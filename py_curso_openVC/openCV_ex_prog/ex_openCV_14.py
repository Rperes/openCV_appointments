import cv2
import numpy as np

imagem = cv2.imread('imgs/ponte.jpg')
cv2.imshow("Original", imagem)
mascara = np.zeros(imagem.shape[:2], dtype = "uint8")

(cX, cY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 255, -1)
img_com_mascara = cv2.bitwise_and(imagem, imagem, mask = mascara)
cv2.imshow("Mascara aplicada a imagem", img_com_mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
