import cv2
import numpy as np

img = cv2.imread('imgs/ponte.jpg')

img = img[::2, ::2] # Diminui a imagem
suave = np.vstack([
    np.hstack([img,
               cv2.medianBlur(img,  3)]),
    np.hstack([cv2.medianBlur(img,  5),
               cv2.medianBlur(img,  7)]),
    np.hstack([cv2.medianBlur(img,  9),
               cv2.medianBlur(img, 11)]),])
cv2.imshow("Imagem original e suavisadas pela mediana", suave)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
