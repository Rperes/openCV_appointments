import cv2

imagem = cv2.imread('imgs/ponte.jpg')

cv2.imshow('Original', imagem)  
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gray', gray) 
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) 
cv2.imshow('HSV', hsv)
lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b*', lab) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1) 
