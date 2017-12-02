import cv2 
imagem = cv2.imread('imgs/ponte.jpg')

for y in range(0, imagem.shape[0]): 
	for x in range(0, imagem.shape[1]):    
		imagem[y, x] = (255,0,0)
	
cv2.imshow("Imagem modificada", imagem) 

# espera por pressionar qualquer tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac força o destroyAllWindows.
cv2.waitKey(1)  
