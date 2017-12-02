import cv2

imagem = cv2.imread('imgs/ponte.jpg')
cv2.imshow('Original', imagem)

altura   = imagem.shape[0]
largura  = imagem.shape[1]
porpocao = float(altura)/float(largura)

largura_nova = 220 #pixeis
altura_nova  = int(largura_nova * porpocao)
tamanho_novo = (largura_nova, altura_nova)

imagem_redimensionada = cv2.resize(imagem, tamanho_novo , interpolation = cv2.INTER_AREA)
cv2.imshow('Imagem redimensionada', imagem_redimensionada)

cv2.waitKey(0)
cv2.destroyAllWindows()

# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)

