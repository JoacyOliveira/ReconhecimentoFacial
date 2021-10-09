import cv2,os
from .models import Imagem

cascade = os.path.abspath("rec/HaarCascade/haarcascade_frontalface_default.xml")

face_cascade = cv2.CascadeClassifier(cascade)

def analisar_imagem():

    ultimaimagem = Imagem.objects.last()
    nomeimagem = ultimaimagem.image.name
    imagem = os.path.abspath('media/' + nomeimagem)
    print(cascade)
    print(imagem)
    img = cv2.imread(imagem)
    print(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    try:
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if (len(faces) == 0):
            return False
            print("Não foi")
        else:
            return True

    except:
        print("Não tem face")
