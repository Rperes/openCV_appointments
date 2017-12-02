import cv2
import numpy as np

#img = cv2.imread('carris.jpg')
#img = cv2.imread('ponte.jpg')
#img = cv2.imread('bia.jpg')
img = cv2.imread('imgs/matriz.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)
resultado = np.vstack([
    np.hstack([img, sobelX]),
    np.hstack([sobelY, sobel])
    ])
cv2.imshow("Sobel", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
