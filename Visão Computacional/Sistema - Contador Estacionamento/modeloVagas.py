import cv2
import pickle

img = cv2.imread('estacionamento.png')

vagas = []

#Salvando todas as vagas em um só objeto para gravar
for x in range(69):
    vaga = cv2.selectROI('vagas',img,False)
    cv2.destroyWindow('vagas')
    vagas.append(vaga)

    #Selecionando cada uma das vagas com um retângulo
    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w, y+h),(127,255,0),2)



#Salvando o arquivo fisicamente com a extensão pkl
with open('vagas.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)
    
            