import cv2

#membuat objek untuk menangkap video dari kamera defult
cap = cv2.videoCapture(0) 
#"0" sesuaikan dengan kamera yang digunakan
#"0" biasanya merujuk kepada webcam 
#jika menggunakan cctv rtsp maka dapat mengganti "0" menjadi 
#"rtsp://{username}:{pasword}@{IP}:554/Streaming/Channels/1"

#Memeriksa apakah kamera berhasil dibuka
if not cap.isOpened():
  print("Tidak dapat membuka kamera")
  exit()

while True:
  #membaca satu frame dari kamera
  #'ret' adalah boolean (True/False) yang menandakan frame berhasil dibaca
  #'frame' adalah gambar yang ditangkap

  ret, frame = cap.read()

  if not ret :
    print("tidak dapat menerima frame"
    break
    
  #menampilkan frame dijendela bernama kamera
  cv2.imshow('kamera', frame)
  #tunggu 1 milidetik, dan keluar dari loop jika tombol 'q' ditekan
  if cv2.waitKey(1) == ord('q') :
    break

cap.release()
cv2.destroyAllwindows()

