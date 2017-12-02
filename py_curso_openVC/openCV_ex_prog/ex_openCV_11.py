import cv2

img = cv2.imread('imgs/ponte.jpg')
cv2.imshow("Original", img)
img_redimensionada = img[::2,::2]

cv2.imshow("Imagem redimensionada", img_redimensionada)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
