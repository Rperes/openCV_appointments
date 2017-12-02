import os
import cv2

# Faz a varredura do diretorio imagens buscando arquivos JPG, JPEG e PNG.
diretorio = 'imgs'
arquivos = os.listdir(diretorio)
for a in arquivos:
    if a.lower().endswith('.jpg') or a.lower().endswith('.png') \
            or a.lower().endswith('.jpeg'):

        imgC = cv2.imread(diretorio+'/'+a)
        imgPB = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
        df = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        faces = df.detectMultiScale(
                        imgPB,
                        scaleFactor=1.2,
                        minNeighbors=2,
                        minSize=(30, 30),
                        flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(imgC, (x, y), (x + w, y + h), (0, 255, 255), 2)
        alt = int(float(imgC.shape[0]/float(imgC.shape[1])*640))
        imgC = cv2.resize(imgC, (640, alt), interpolation=cv2.INTER_CUBIC)
        cv2.imshow(str(len(faces))+' face(s) encontrada(s).', imgC)

        cv2.waitKey(0)
        cv2.destroyAllWindows ()
        # On Mac need to force to destroyAllWindows.
        cv2.waitKey(1)