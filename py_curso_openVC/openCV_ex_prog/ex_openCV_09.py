import cv2 
imagem = cv2.imread('imgs/ponte.jpg')

recorte = imagem[100:300, 100:300] 
cv2.imshow("Recorte da imagem", recorte) 
cv2.imwrite('recorte.jpg', recorte)     #salvagarda no disco 

cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac força o destroyAllWindows.
cv2.waitKey(1)
