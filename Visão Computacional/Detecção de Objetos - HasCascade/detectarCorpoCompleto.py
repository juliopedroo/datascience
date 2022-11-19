import cv2

camera = cv2.VideoCapture('video.mp4')
classificador = cv2.CascadeClassifier(r'cascades/cascades/haarcascade_fullbody.xml')


while True:
    check,img = camera.read()

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray,minSize=(50,50), scaleFactor=1.5)

    # criando a Estrutura de Repetição para percorrer o objeto.

    for x, y, l, a in objetos:
        cv2.rectangle(img, (x,y), (x+y,y+a), (27,139,61),2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(10)