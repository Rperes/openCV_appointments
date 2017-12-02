from matplotlib import pyplot as plt
import cv2 

img = cv2.imread('imgs/ponte.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original BW', img) 
h_eq = cv2.equalizeHist(img)
cv2.imshow('Imagem equalizada', h_eq) 

plt.figure(0)
plt.title("Histograma Original") 
plt.xlabel("Intensidade") 
plt.ylabel("Qtde de Pixels") 
plt.hist(img.ravel(), 256, [0,256]) 
plt.xlim([0, 256]) 
plt.show(0)

plt.figure(1)
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)


