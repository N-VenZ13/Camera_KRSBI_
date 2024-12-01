#----------------| ROAD TO KRI 2021 |----------------------#
#--------| 2 Agustus  2019 || M. Zafier Faza  |------------#
#--------| 5 Desember 2020 || Sedry M. Iqbal  |------------#

from time import sleep
from threading import *
import cv2                  #Library Opencv Untuk Mengelola Gambar
import numpy as np          #Untuk operasi vektor dan matriks
import serial               #Library serial untuk komunikasi ata serial RS232
import time                 #Library time untuk waktu / tanggal
import varTrackbar1 as vt    #Library buatan
import socket


def nothing(x):
    pass
def constrain(val, min_val, max_val):           #Fungsi contrain untuk membatasi suatu nila
    return min(max_val, max(min_val, val))      #Fungsi return untuk mengembalikan nilai ke awal
#arduino = serial.Serial('COM3', 500000,timeout=.1) #Untuk komunikasi ke arduino

time.sleep(1)
# cap = cv2.VideoCapture(0)  #Untuk memanggil kamera Depan
cap2= cv2.VideoCapture(0) #Untuk memanggil kamera Atas
# vt.BolaTrackbarD(0,116,16)     #Untuk variabel nilai hsv bola kamera depan
# vt.LapanganTrackbarD(54,59,73) #Untuk variabel nilai hsv Lapangan kamera depan
vt.BolaTrackbarA(0,137,132)    #Untuk variabel nilai hsv bola kamera atas
vt.LapanganTrackbarA(54,59,73) #Untuk variabel nilai hsv Lapangan4 kamera atas




class kamera(Thread):
    def run(self):       
        while True:
            # ret1,frame = cap.read()         # Membuat Tangkap bingkai demi bingkai Kamera depan
            ret2,frameUp = cap2.read()      # Membuat Tangkap bingkai demi bingkai Kamera Atas
            frameUp = cv2.flip(frameUp,1)   # Mengatur derajat putar Tampilan Kamera

            # vt.RacikBolaD(frame)
            # vt.RacikLapanganD(frame)
            vt.RacikBolaA(frameUp)
            vt.RacikLapanganA(frameUp)
            
            # res2 = cv2.bitwise_or(vt.orangeD, vt.hijauD)  #Mencampur closing orange + putih
            res2_Up = cv2.bitwise_or(vt.orange_A, vt.hijau_A)

            # contourBola = cv2.findContours(vt.orangeD, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2] #Untuk Mendapatkan kontur atau struktur dari gambar binary sebelumnya yang disimpan kedalam bentuk list
            # if len(contourBola) > 0:
            #     area = max(contourBola, key = cv2.contourArea)  #Temukan kontur dengan area maks
            #     xx, yy, w, h = cv2.boundingRect(area)           #Buat persegi panjang pembatas di sekitar kontur
            #     ((x, y), radius) = cv2.minEnclosingCircle(area) #Mencari radius untuk menggambar lingkaran
            #     approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True) #Untuk mendeteksi contour dengan bentuk tertentu
            #     pusat = (int(x), int(y))
            #     pusat_str = (int(x) - 35, int(y) + 15)
            #     koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")
            #     font = cv2.FONT_HERSHEY_SIMPLEX
            #     maxxx = (xx+w)+3
            #     maxyy = (yy+h)+3
            #     huxx = xx+int(w/2)
            #     huyy = yy+int(h/2)
            #     maxXX = constrain(maxxx, 0, 639)
            #     maxYY = constrain(maxyy, 0, 479)
            #     huXX = constrain(huxx, 0, 639)
            #     huYY = constrain(huyy, 0, 479)


            #  # |____________________| Membaca Warna Orange Kamera|______________________| 
            # # # index 640 is out of bounds for axis 1 with size 640           
            #     if area is not None:
            #         if np.any(res2[maxYY,maxXX]) or  np.any(res2[huYY,maxXX]) or  np.any(res2[maxYY,huXX]) or  np.any(res2[maxYY,xx-5]) or  np.any(res2[huYY,xx-5]) != 0:       ## pengecekan kiri atas bola adalah lapangan
            #     # if  np.any(res2[yy-5,xx]) or np.any(res2[yy,xx-5]) or np.any(res2[yy-5,xx+int(w*1/3)]) or np.any(res2[yy-5,xx+int(w/2)]) or np.any(res2[yy-5,xx+int(w*3/4)])  or np.any(res2[yy+int(h*1/4),xx-5])   or np.any(res2[yy+int(h/2),xx-5])   or np.any(res2[yy+int(h*3/4),xx-5]) or np.any(res2[maxYY,maxXX]) != 0:       ## pengecekan kiri atas bola adalah lapangan
            #             cv2.rectangle(frame, (xx,yy), (xx+w, yy+h), (0,165,255), 2)              #Membuat kotak pada gambar maupun kamera  real-time
            #             cv2.putText(frame, koordinat_str, pusat_str,font, 0.5, (255,255,255), 2) #Menempatkan text
            #             cv2.line(frame, (330,490),pusat, (255,255,255), 2)                       #Membuat Garis                                   
            #             cv2.line(frame, (pusat),(int(xx-5), int(huYY)), (0,255,0), 1)
            #             cv2.line(frame, (pusat),(int(xx-5), int(maxYY)), (0,255,0), 1)
            #             cv2.line(frame, (pusat),(int(huXX), int(maxYY)), (0,255,0), 1)
            #             cv2.line(frame, (pusat),(int(maxXX), int(huYY)), (0,255,0), 1)
            #             cv2.line(frame, (pusat),(int(maxXX), int(maxYY)), (0,255,0), 1)
            #             print("BOLA TERDETEKSI")
            #             #arduino.write(str(x).encode())  #Untuk Mengirim data X ke arduino
            #             #arduino.write('x'.encode())     
            #             #arduino.write(str(y).encode())  #Untuk Mengirim data y ke arduino
            #             #arduino.write('y'.encode())
            #         else :
            #             cv2.drawContours(frame, [approx], 0, (0, 0, 255), 2)
            #             print("BOLA NOTHING")
            #             #arduino.write('0'.encode())
            #             #arduino.write('x'.encode())
            #             #arduino.write('0'.encode())
            #             #arduino.write('y'.encode())
            # elif len(contourBola) == 0 :
            #     print("BOLA NOTHING")
            #     #arduino.write('0'.encode())
            #     #arduino.write('x'.encode())
            #     #arduino.write('0'.encode())
            #     #arduino.write('y'.encode())

            # Tambahkan pengecekan sebelum menggunakan approx untuk menggambar kontur
            contourBola_omni = cv2.findContours(vt.orange_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            if len(contourBola_omni) > 0:
                area = max(contourBola_omni, key=cv2.contourArea)
                xx, yy, w, h = cv2.boundingRect(area)
                ((x, y), radius) = cv2.minEnclosingCircle(area)
                approx = cv2.approxPolyDP(area, 0.001 * cv2.arcLength(area, True), True)
                
                # Hanya gunakan approx jika tidak None atau tidak kosong
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
                    else:
                        cv2.drawContours(frameUp, [approx], 0, (0, 0, 255), 2)
                        print("BOLA NOTHING")
            else:
                # Jangan panggil drawContours jika approx tidak diinisialisasi
                print("BOLA NOTHING")








            # contourBola_omni = cv2.findContours(vt.orange_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            # if len(contourBola_omni) > 0:
            #    area = max(contourBola_omni, key = cv2.contourArea)
            #    xx, yy, w, h = cv2.boundingRect(area)
            #    ((x, y), radius) = cv2.minEnclosingCircle(area)
            #    approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
            #    pusat = (int(x), int(y))
            #    pusat_str = (int(x) - 35, int(y) + 15)
            #    koordinat_str = ("(" + str(int(x)) + "," + str(int(y)) + ")")
            #    font = cv2.FONT_HERSHEY_SIMPLEX
            #    maxxx = (xx+w)+3
            #    maxyy = (yy+h)+3
            #    minxx = (xx+w)-3
            #    minyy = (yy+h)-3
            #    huxx = xx+int(w/2)
            #    huyy = yy+int(h/2)

            #    maxXX = constrain(maxxx, 0, 639)
            #    maxYY = constrain(maxyy, 0, 479)
            #    huXX = constrain(huxx, 0, 639)
            #    huYY = constrain(huyy, 0, 479)

                # |____________________| Membaca Warna Orange Kamera OmniVision|______________________| 
                # index 640 is out of bounds for axis 1 with size 640
            #    if area is not None:
            #        if np.any(res2_Up[maxYY,maxXX]) or np.any(res2_Up[huYY,maxXX]) or  np.any(res2_Up[maxYY,huXX]) or  np.any(res2_Up[maxYY,xx-5]) or  np.any(res2_Up[huYY,xx-5]) or  np.any(res2_Up[yy-5,xx-5]) or  np.any(res2_Up[yy-5,huXX]) or  np.any(res2_Up[yy-5,maxXX])  != 0:       ## pengecekan kiri atas bola adalah lapangan
                        # if  np.any(res2[yy-5,xx]) or np.any(res2[yy,xx-5]) or np.any(res2[yy-5,xx+int(w*1/3)]) or np.any(res2[yy-5,xx+int(w/2)]) or np.any(res2[yy-5,xx+int(w*3/4)])  or np.any(res2[yy+int(h*1/4),xx-5])   or np.any(res2[yy+int(h/2),xx-5])   or np.any(res2[yy+int(h*3/4),xx-5]) or np.any(res2[maxYY,maxXX]) != 0:       ## pengecekan kiri atas bola adalah lapangan
                            # cv2.rectangle(frameUp, (xx,yy), (xx+w, yy+h), (0,165,255), 2)
                            # cv2.putText(frameUp, koordinat_str, pusat_str,font, 0.5, (255,255,255), 2)
                            # cv2.line(frameUp, (335,250),pusat, (255,255,255), 2)
                            # cv2.line(frameUp, (pusat),(int(xx-5), int(huYY)), (0,255,0), 1)
                            # cv2.line(frameUp, (pusat),(int(xx-5), int(maxYY)), (0,255,0), 1)
                            # cv2.line(frameUp, (pusat),(int(huXX), int(maxYY)), (0,255,0), 1)
                            # cv2.line(frameUp, (pusat),(int(maxXX), int(huYY)), (0,255,0), 1)
                            # cv2.line(frameUp, (pusat),(int(maxXX), int(maxYY)), (0,255,0), 1)
                            # print("BOLA TERDETEKSI")
                            # arduino.write(str(x).encode())
                            # arduino.write('v'.encode())
                            # arduino.write(str(y).encode())
                            # arduino.write('w'.encode())
            #    else :
            #        cv2.drawContours(frameUp, [approx], 0, (0, 0, 255), 2)
            #        print("BOLA TIDAK TERDETEKSI")
                    #   arduino.write('0'.encode())
                    #   arduino.write('v'.encode())
                    #   arduino.write('0'.encode())
                    #   arduino.write('w'.encode())
            # elif len(contourBola_omni) == 0 :
            #     cv2.drawContours(frameUp, [approx], 0, (0, 0, 255), 2)
            #     print("BOLA TIDAK TERDETEKSI")
                # arduino.write('0'.encode())
                # arduino.write('v'.encode())
                # arduino.write('0'.encode())
                # arduino.write('w'.encode())
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==  
            # contourLapangan = cv2.findContours(vt.hijauD, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            # if len(contourLapangan) > 0:
            #     area = max(contourLapangan, key = cv2.contourArea)
            #     approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
            #     if area is not None: 
            #         cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)  #Untuk menggambar kontur fungsi 
                    # cv2.line(frame, (pusat),(int(320), int(240)), (0,255,0), 1)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==  
            contourLapangan_omni = cv2.findContours(vt.hijau_A, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
            if len(contourLapangan_omni) > 0:
                area = max(contourLapangan_omni, key = cv2.contourArea)
                approx = cv2.approxPolyDP(area, 0.001*cv2.arcLength(area, True), True)
                if area is not None: 
                    cv2.drawContours(frameUp, [approx], 0, (0, 255, 0), 2)
        ##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==
                

            # cv2.imshow("frame", frame)                  #Untuk menampilkan gambar di jendela WIndows Frame Kamera Depan
            cv2.imshow("frame_omni", frameUp)           #Untuk menampilkan gambar di jendela WIndows Frame Kamera Atas
            # cv2.imshow("Lapangan", vt.hijauD)           #Untuk menampilkan gambar di jendela WIndows Lapangan Kamera Depan
            # cv2.imshow("Mask_OR", res2)                 #Untuk menampilkan gambar di jendela WIndows Mask Or Kamera Depan
            # cv2.imshow("BOLA", vt.orangeD)              #Untuk menampilkan gambar di jendela WIndows Bola Kamera Depan
            cv2.imshow("Lapangan_OMNI", vt.hijau_A)     #Untuk menampilkan gambar di jendela WIndows Lapangan Kamera Atas
            #cv2.imshow("Mask_OR_OMNI", res2_Up)         #Untuk menampilkan gambar di jendela WIndows Mask Or Kamera Atas
            cv2.imshow("BOLA_OMNI", vt.orange_A)        #Untuk menampilkan gambar di jendela WIndows Bola Kamera Atas
            key = cv2.waitKey(1)
            if key == 27:
                cap2.release()
                cv2.destroyAllWindows()
                break
            

class komunikasi(Thread):
    def run(self):
        while True:
            IPADDR = '192.168.100.51'        #IP Koneksi Basestation , menentukan ip address dan port
            PORT = 28097                     #Port Koneksi Basestation
            ADDR = (IPADDR,PORT)
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #membuat socket
            s.bind(ADDR)                                        #bind
            d, addr = s.recvfrom(1024)
            do = d.decode('utf-8')
            print ("MASOOOOOOOOOOOOOOOOOK")
            #arduino.write(str(do).encode('utf-8'))
            #arduino.write('>'.encode('utf-8'))
            
            s.close()
            sleep(1)



# t2 = komunikasi()
t1 = kamera()

# t2.start()
t1.start()


