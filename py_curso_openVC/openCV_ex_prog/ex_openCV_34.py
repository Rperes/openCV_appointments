import cv2

# Carrega arquivo e converte para tons de cinzento
img = cv2.imread('imgs/caras.jpg')
iPB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Criacao do detector de faces
df = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Executa a detecao
faces = df.detectMultiScale(iPB, scaleFactor=1.05, minNeighbors=7, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

# Desenha retangulos amarelos na iamgem original (colorida)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# Exibe imagem. Titulo da janela exibe numero de faces
cv2.imshow(str(len(faces))+' face(s) encontrada(s) ', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# On Mac need to force to destroyAllWindows.
cv2.waitKey(1)
