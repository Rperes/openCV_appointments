import cv2 
imagem = cv2.imread('imgs/ponte.jpg')
cv2.imshow("Original", imagem) 

#flip_horinzontal = imagem[:,::-1]   #comando equivalente abaixo 
flip_horinzontal = cv2.flip(imagem, 1)  
cv2.imshow("Flip horizontal", flip_horinzontal) 

#flip_vertical = imagem[::-1,:] #comando equivalente abaixo 
flip_vertical = cv2.flip(imagem, 0)  
cv2.imshow("Flip verical", flip_vertical) 

#flip_hv = imagem[::-1,::-1]      #comando equivalente abaixo  
flip_hv = cv2.flip(imagem, -1) 
cv2.imshow("Flip Horizontal e Vertical", flip_hv) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
