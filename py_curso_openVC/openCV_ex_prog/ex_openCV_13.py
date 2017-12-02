import cv2 
imagem = cv2.imread('imgs/ponte.jpg')
cv2.imshow("Original", imagem)

(alt, lar) = imagem.shape[:2] #captura altura e largura 
centro = (lar // 2, alt // 2) #acha o centro  
M = cv2.getRotationMatrix2D(centro, 45, 1.0)  #45 graus 

img_rotacionada = cv2.warpAffine(imagem, M, (lar, alt))  
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
