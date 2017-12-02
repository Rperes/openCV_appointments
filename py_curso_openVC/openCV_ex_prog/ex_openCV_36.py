import cv2

# funcao para redimensionar uma imagem
def redim(img, largura):
    alt = int(float(img.shape[0])/float(img.shape[1])*largura)
    img = cv2.resize(img, (largura, alt), interpolation =cv2.INTER_AREA)
    return img

# Cria o detector de faces baseado no XML
df = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Abre um video gravado em disco
camera = cv2.VideoCapture('video.mov')

# Tambem e possivel abrir a proprio webcam
# do sistema para isso segue codigo abaixo
# camera = cv2.VideoCapture(0)

while True:
    # read() retorna 1-Se houve sucesso e 2-O proprio frame
    (sucesso, frame) = camera.read()
    if not sucesso: # final do video
        break

    # reduz tamanho do frame para acelerar processamento
    frame = redim(frame, 320)

    # converte para tons de cinza
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecta as faces no frame
    faces = df.detectMultiScale(frame_pb,
            scaleFactor = 1.1,
            minNeighbors=3,
            minSize=(20,20),
            flags=cv2.CASCADE_SCALE_IMAGE)
    frame_temp = frame.copy()
    for (x, y, lar, alt) in faces:
        cv2.rectangle(frame_temp,
            (x, y),
            (x + lar, y + alt),
            (0, 255, 255), 2)
    # Exibe um frame redimensionado (com perca de qualidade)
    cv2.imshow("Encontrando faces...", redim(frame_temp, 640))

    # Espera que a tecla 's' seja pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# fecha streaming
camera.release()
cv2.destroyAllWindows()
