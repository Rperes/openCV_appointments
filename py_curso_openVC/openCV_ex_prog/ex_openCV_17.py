import cv2  
imagem = cv2.imread('imgs/ponte.jpg')

cv2.imshow("Original", imagem)  
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)  
cv2.imshow("Vermelho", canalVermelho) 
cv2.imshow("Verde", canalVerde) 
cv2.imshow("Azul", canalAzul) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
