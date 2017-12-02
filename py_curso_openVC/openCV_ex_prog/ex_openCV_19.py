import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('imgs/memo.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Preto Branco', imagem)

h = cv2.calcHist([imagem], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histograma P&B')
plt.xlabel('Intensidade')
plt.ylabel('Quantidade de Pixels')
plt.xlim([0, 256])
plt.hist(imagem.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
