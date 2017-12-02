# Importacao das bibliotecas
import cv2
   
# Leitura da imagem com a funcao imread()
imagem = cv2.imread('imgs/ronaldo_in.jpg')

print('Largura em pixels: ', imagem.shape[1])  # largura da imagem.    
print('Altura em pixels: ' , imagem.shape[0])  # altura da imagem. 
print('Numero de canais: ' , imagem.shape[2])  # numero de canais da imagem.

cv2.imshow("Imagem original", imagem)           # atribui nome a janela

# salvaguardar a imagem no disco com funcao imwrite()
cv2.imwrite('ronaldo_out.jpg', imagem)

# espera por pressionar qualquer tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
# no Mac forca o destroyAllWindows.
cv2.waitKey(1)  
