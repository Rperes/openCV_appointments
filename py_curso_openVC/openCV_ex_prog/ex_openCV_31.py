
import cv2
import numpy as np

img = cv2.imread('imgs/ponte.jpg')                # importa a imagem do ficheiro
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte para bW
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
resultado = np.vstack([img, lap])

cv2.imshow("Filtro Laplaciano", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
