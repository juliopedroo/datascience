# Import biblioteca do OpenCV
import cv2

#Chamando e abrindo a WEBCAM
camera = cv2.VideoCapture(0)   #Com 0, captura imagem da própria camera

#Classificador para detecção de objetos
classificador = cv2.CascadeClassifier(r'cascades/cascades/haarcascade_eye.xml')

#Desenvolvimento do projeto
while True:
    check,img = camera.read() #Capturando imagem da câmera
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #imagem em tons de cinza
    objetos = classificador.detectMultiScale(imgGray)   #detectando os elementos do rosto, se concentrando no elemento especialista do HaarCascade, no caso, olhos.

    #Criando retângulos para marcação dos olhos
    for x ,y,l,a in objetos:
        cv2.rectangle(img,(x,y),(x+l, y+a),(255,0,0), 2)

    cv2.imshow('Imagem', img)    # imshow() é usado para exibir uma imagem em uma janela
    cv2.waitKey(1)