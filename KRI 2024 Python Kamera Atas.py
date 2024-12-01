from time import sleep
from threading import *
import cv2                  
import numpy as np          
import serial               
import time                 
import varTrackbar1 as vt    
import socket


def nothing(x):
    pass

def constrain(val, min_val, max_val):           
    return min(max_val, max(min_val, val))      

# arduino = serial.Serial('COM7', 500000, timeout=.1)  # Untuk komunikasi ke arduino



time.sleep(1)
cap2 = cv2.VideoCapture(0) 
vt.BolaTrackbarA(0, 73, 60)    
vt.LapanganTrackbarA(54, 59, 73) 

class kamera(Thread):
    def run(self):       
        while True:
            ret2, frameUp = cap2.read()      
            frameUp = cv2.flip(frameUp, 1)   

            vt.RacikBolaA(frameUp)
            vt.RacikLapanganA(frameUp)
            
            res2_Up = cv2.bitwise_or(vt.orange_A, vt.hijau_A)

            contourBola_omni = cv2.findContours(vt.orange_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            if len(contourBola_omni) > 0:
                area = max(contourBola_omni, key=cv2.contourArea)
                xx, yy, w, h = cv2.boundingRect(area)
                ((x, y), radius) = cv2.minEnclosingCircle(area)
                approx = cv2.approxPolyDP(area, 0.001 * cv2.arcLength(area, True), True)
                
                if approx is not None and len(approx) > 0:
                    pusat = (int(x), int(y))
                    pusat_str = (int(x) - 35, int(y) + 15)
                    koordinat_str = "(" + str(int(x)) + "," + str(int(y)) + ")"
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    maxxx = (xx + w) + 3
                    maxyy = (yy + h) + 3
                    huxx = xx + int(w / 2)
                    huyy = yy + int(h / 2)

                    maxXX = constrain(maxxx, 0, 639)
                    maxYY = constrain(maxyy, 0, 479)
                    huXX = constrain(huxx, 0, 639)
                    huYY = constrain(huyy, 0, 479)

                    if np.any(res2_Up[maxYY, maxXX]) or np.any(res2_Up[huYY, maxXX]) or np.any(res2_Up[maxYY, huXX]) or np.any(res2_Up[maxYY, xx - 5]) or np.any(res2_Up[huYY, xx - 5]) != 0:
                        cv2.rectangle(frameUp, (xx, yy), (xx + w, yy + h), (0, 165, 255), 2)
                        cv2.putText(frameUp, koordinat_str, pusat_str, font, 0.5, (255, 255, 255), 2)
                        cv2.line(frameUp, (335, 250), pusat, (255, 255, 255), 2)
                        print("BOLA TERDETEKSI")
                        
                        # arduino.write(str(x).encode())  # Mengirim data X ke arduino
                        # arduino.write('x'.encode())     
                        # arduino.write(str(y).encode())  # Mengirim data Y ke arduino
                        # arduino.write('y'.encode())
                    else:
                        cv2.drawContours(frameUp, [approx], 0, (0, 0, 255), 2)
                        print("BOLA NOTHING")
                        
                        # arduino.write('0'.encode())
                        # arduino.write('x'.encode())
                        # arduino.write('0'.encode())
                        # arduino.write('y'.encode())
            else:
                print("BOLA NOTHING")
                
                # arduino.write('0'.encode())
                # arduino.write('x'.encode())
                # arduino.write('0'.encode())
                # arduino.write('y'.encode())

            contourLapangan_omni = cv2.findContours(vt.hijau_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            if len(contourLapangan_omni) > 0:
                area = max(contourLapangan_omni, key=cv2.contourArea)
                approx = cv2.approxPolyDP(area, 0.001 * cv2.arcLength(area, True), True)
                if area is not None: 
                    cv2.drawContours(frameUp, [approx], 0, (0, 255, 0), 2)

            cv2.imshow("frame_omni", frameUp)           
            cv2.imshow("Lapangan_OMNI", vt.hijau_A)     
            cv2.imshow("BOLA_OMNI", vt.orange_A)        
            key = cv2.waitKey(1)
            if key == 27:
                cap2.release()
                cv2.destroyAllWindows()
                break

class komunikasi(Thread):
    def run(self):
        while True:
            IPADDR = '192.168.100.51'        
            PORT = 28097                     
            ADDR = (IPADDR, PORT)
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
            s.bind(ADDR)                                        
            d, addr = s.recvfrom(1024)
            do = d.decode('utf-8')
            print("MASOOOOOOOOOOOOOOOOOK")
            
            # arduino.write(str(do).encode('utf-8'))
            # arduino.write('>'.encode('utf-8'))
            
            s.close()
            sleep(1)

t2 = komunikasi()
t1 = kamera()

t2.start()
t1.start()

