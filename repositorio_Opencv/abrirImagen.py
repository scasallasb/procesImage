import cv2 

#comando para leer imagen 
im = cv2.imread('lena.jpeg', 1)

# mostrar una imagen
cv2.imshow('imagen lena', im)

#Guardar una imagen 
cv2.imwrite('imagenG.jpg',im)

#comando para detener la imagen
cv2.waitKey(0)
