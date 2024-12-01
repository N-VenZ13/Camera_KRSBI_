from threading import *
import cv2                  #Library Opencv Untuk Mengelola Gambar
import numpy as np          #Untuk operasi vektor dan matriks

def nothing(x):
    pass

# cv2.namedWindow('Setting Kamera Depan', cv2.WINDOW_NORMAL)  #Untuk membuat tampilan pada windows
cv2.namedWindow('Setting Kamera Atas', cv2.WINDOW_NORMAL)


# def BolaTrackbarD(H_min,S_min,V_min):
#     maximum = 255
#     h_max = 179
#     cv2.createTrackbar('H_Bola','Setting Kamera Depan',H_min,h_max,nothing)      #Buat trackbar untuk perubahan warna
#     cv2.createTrackbar('S_Bola','Setting Kamera Depan',S_min,maximum,nothing)
#     cv2.createTrackbar('V_Bola','Setting Kamera Depan',V_min,maximum,nothing)

# def LapanganTrackbarD(H_min,S_min,V_min):
#     maximum = 255
#     h_max = 179
#     cv2.createTrackbar('H_Lapangan','Setting Kamera Depan',H_min,h_max,nothing)      #Buat trackbar untuk perubahan warna
#     cv2.createTrackbar('S_Lapangan','Setting Kamera Depan',S_min,maximum,nothing)
#     cv2.createTrackbar('V_Lapangan','Setting Kamera Depan',V_min,maximum,nothing)

def BolaTrackbarA(H_min,S_min,V_min):   
   maximum = 255
   h_max = 179
   cv2.createTrackbar('H_Bola_omni','Setting Kamera Atas',H_min,h_max,nothing)      #Buat trackbar untuk perubahan warna
   cv2.createTrackbar('S_Bola_omni','Setting Kamera Atas',S_min,maximum,nothing)
   cv2.createTrackbar('V_Bola_omni','Setting Kamera Atas',V_min,maximum,nothing)

def LapanganTrackbarA(H_min,S_min,V_min):
   maximum = 255
   h_max = 179
   cv2.createTrackbar('H_Lapangan_omni','Setting Kamera Atas',H_min,h_max,nothing)      #Buat trackbar untuk perubahan warna
   cv2.createTrackbar('S_Lapangan_omni','Setting Kamera Atas',S_min,maximum,nothing)
   cv2.createTrackbar('V_Lapangan_omni','Setting Kamera Atas',V_min,maximum,nothing)

#===================================================================================================================================#
# def RacikBolaD(frame):
#     H_Bola = cv2.getTrackbarPos('H_Bola','Setting Kamera Depan')  #Membaca posisi trackbar untuk semua
#     S_Bola = cv2.getTrackbarPos('S_Bola','Setting Kamera Depan')
#     V_Bola = cv2.getTrackbarPos('V_Bola','Setting Kamera Depan')
#     kernel = np.ones((10, 10), np.uint8)                            #Untuk  mengembalikan array baru dari bentuk dan jenis yang diberikan, diisi dengan nilai satu

#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                  #untuk meng-convert image matrix ke grayscale dengan parameter cv2.COLOR_BGR2GRAY
  
#     global orangeD #Mengembalikan dictionary yang berisi semua variabel
#     lowerO = np.array([H_Bola,S_Bola,V_Bola])
#     upperO = np.array([31,255,255])
#     orangeD = cv2.inRange(hsv,lowerO,upperO)
#     orangeD = cv2.erode(orangeD, kernel)
#     orangeD = cv2.morphologyEx(orangeD, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
#     orangeD = cv2.morphologyEx(orangeD, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
#     return orangeD
#===================================================================================================================================#
# def RacikLapanganD(frame):
#     H_Lapangan = cv2.getTrackbarPos('H_Lapangan','Setting Kamera Depan')
#     S_Lapangan = cv2.getTrackbarPos('S_Lapangan','Setting Kamera Depan')
#     V_Lapangan = cv2.getTrackbarPos('V_Lapangan','Setting Kamera Depan')
#     kernel = np.ones((5, 5), np.uint8)
    
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     global hijauD
#     lowerH = np.array([H_Lapangan,S_Lapangan,V_Lapangan])
#     upperH = np.array([102,255,255])
#     hijauD = cv2.inRange(hsv,lowerH,upperH)
#     hijauD = cv2.erode(hijauD, kernel)
#     hijauD = cv2.morphologyEx(hijauD, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
#     hijauD = cv2.morphologyEx(hijauD, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
#     return hijauD
#===================================================================================================================================#
def RacikBolaA(frameUp):
    # Gunakan nama yang benar dari trackbar
    H_Bola_Omni = cv2.getTrackbarPos('H_Bola_omni','Setting Kamera Atas')
    S_Bola_Omni = cv2.getTrackbarPos('S_Bola_omni','Setting Kamera Atas')
    V_Bola_Omni = cv2.getTrackbarPos('V_Bola_omni','Setting Kamera Atas')
    kernel = np.ones((5, 5), np.uint8)

    hsv = cv2.cvtColor(frameUp, cv2.COLOR_BGR2HSV)
   
    global orange_A
    lowerO_omni = np.array([H_Bola_Omni, S_Bola_Omni, V_Bola_Omni])
    upperO_omni = np.array([31,255,255])
    orange_A = cv2.inRange(hsv, lowerO_omni, upperO_omni)
    orange_A = cv2.erode(orange_A, kernel)
    orange_A = cv2.morphologyEx(orange_A, cv2.MORPH_OPEN, kernel)  # Membuat Opening
    orange_A = cv2.morphologyEx(orange_A, cv2.MORPH_CLOSE, kernel) # Membuat Closing
    return orange_A

#===================================================================================================================================#
def RacikLapanganA(frameUp):
   H_Lapangan_Omni = cv2.getTrackbarPos('H_Lapangan_omni','Setting Kamera Atas')
   S_Lapangan_Omni = cv2.getTrackbarPos('S_Lapangan_omni','Setting Kamera Atas')
   V_Lapangan_Omni = cv2.getTrackbarPos('V_Lapangan_omni','Setting Kamera Atas')
   kernel = np.ones((5, 5), np.uint8)
    
   hsv = cv2.cvtColor(frameUp, cv2.COLOR_BGR2HSV)
    
   global hijau_A
   lowerH_omni = np.array([H_Lapangan_Omni,S_Lapangan_Omni,V_Lapangan_Omni])
   upperH_omni = np.array([102,255,255])
   hijau_A = cv2.inRange(hsv,lowerH_omni,upperH_omni)
   hijau_A = cv2.erode(hijau_A, kernel)
   hijau_A = cv2.morphologyEx(hijau_A, cv2.MORPH_OPEN, kernel)           #Membuat Opening (yaitu mengurangi noise di luar kontour warna)
   hijau_A = cv2.morphologyEx(hijau_A, cv2.MORPH_CLOSE, kernel)        #Membuat Closing (yaitu menutupi lobang lobang di dalam kontour warna)
   return hijau_A

#===================================================================================================================================#







