import cv2
import numpy as np

img = cv2.imread('imgs/ponte.jpg')

img = img[::2, ::2] # Diminui a imagem
suave = np.vstack([
    np.hstack([img,
               cv2.bilateralFilter(img,  3, 21, 21)]),
    np.hstack([cv2.bilateralFilter(img,  5, 35, 35),
               cv2.bilateralFilter(img,  7, 49, 49)]),
    np.hstack([cv2.bilateralFilter(img,  9, 63, 63),
               cv2.bilateralFilter(img, 11, 77, 77)]), ])
cv2.imshow("Imagem original e suavisadas pela mediana", suave)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
