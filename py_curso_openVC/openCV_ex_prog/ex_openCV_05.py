import cv2 
imagem = cv2.imread('imgs/ponte.jpg')

for y in range(0, imagem.shape[0], 10):    #percorre linhas   
   for x in range(0, imagem.shape[1], 10): #percorre colunas     
      imagem[y:y+5, x: x+5] = (0,255,255) 

cv2.imshow('Imagem modificada', imagem) 

cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac força o destroyAllWindows.
cv2.waitKey(1)
