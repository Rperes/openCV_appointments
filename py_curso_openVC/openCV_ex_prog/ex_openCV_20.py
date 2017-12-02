import cv2
from matplotlib import pyplot as plt

img = cv2.imread('imgs/memo.jpg', -1)
cv2.imshow('Ponte', img)

color = ('b', 'g', 'r')

plt.figure()
plt.title('Histograma Colorido')
plt.xlabel('Intensidade')
plt.ylabel('Numero de Pixels')

for channel, col in enumerate(color):
    historico = cv2.calcHist([img], [channel], None, [256], [0, 256])
    plt.plot(historico, color=col)
    plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
