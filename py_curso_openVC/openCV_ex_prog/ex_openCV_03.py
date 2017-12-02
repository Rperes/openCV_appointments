import cv2 
imagem = cv2.imread('imgs/ponte.jpg')

for y in range(0, imagem.shape[0]):      #percorre linhas   
    for x in range(0, imagem.shape[1]):  #percorre colunas     
      imagem[y, x] = (x%256,y%256,x%256)
      
cv2.imshow('Imagem modificada', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac força o destroyAllWindows.
cv2.waitKey(1)  
