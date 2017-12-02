import cv2

imagem = cv2.imread('imgs/ponte.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(imagem,'OpenCV',(15,65), fonte, 2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("Ponte", imagem) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac força o destroyAllWindows.
cv2.waitKey(1) 
