import cv2
import numpy as np

img = cv2.imread('imgs/carris.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img = img[::2, ::2] # Diminui a imagem
suave = suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin)  = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)
resultado = np.vstack([
            np.hstack([suave, bin]),
            np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
            ])
cv2.imshow("Binarizacao da imagem", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)