import cv2 # Biblioteca OpenCV
import os # Biblioteca para operações do sistema
import time # Biblioteca de tempo
from picamera2 import Picamera2 # Biblioteca da câmera da Raspberry Pi
from email.message import EmailMessage #biblioteca para enviar email
import smtplib




from_email_addr = "ep4ce30f23c7@gmail.com"
from_email_password = "mfidgzadlwqoifzu"
to_email_addr = "konrad.aleixo@usp.br"
email_subject = "Foto da pratica"
email_body = "Foto da pratica"

def send_email():
    msg = EmailMessage()
    msg.set_content(email_body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = email_subject
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_password)
    server.send_message(msg)
    server.quit()
    print('Email Enviado')
    sleep(5)

face_detector = cv2.CascadeClassifier("/home/sel/haarcascade_frontalface_default.xml")
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640, 480)}))
picam2.start()

# Define o diretório onde as imagens com rostos detectados serão armazenadas
output_directory = "rostos_detectados"

# Cria o diretório, se ele não existir
os.makedirs(output_directory, exist_ok=True)

#parametros para a escrita do texto na imagem

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#coordenadas da posicao do texto
org = (0, 0)

#fontScale
fontScale = 0.5

#cor
color = (0, 255, 0)

#grossura da linha
thickness = 2

# Loop para captura e detecção de rostos
while True:
    im = picam2.capture_array()
    # Captura um quadro da câmera e armazena na variável

    # Converte a imagem colorida para escala de cinza
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Usa o classificador em cascata para detectar rostos na imagem em escala de cinza

    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    # Loop para processar cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenha um retângulo verde ao redor do rosto na imagem original
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0))

        # Gera um nome de arquivo único com base no carimbo de data/hora
        timestamp = int(time.time())
        filename = os.path.join(output_directory, f"face_{timestamp}.jpg")

        # Salva apenas a porção da imagem que contém o rosto detectado como um arquivo JPEG

        cv2.imwrite(filename, img[y:y+h, x:x+w])
        
        #manda email com a foto
        
        send_email()

        # Exibe a imagem com os retângulos desenhados em uma janela com o título "Camera"

        cv2.imshow("Camera", im)

        # Aguarda 1 milissegundo antes de continuar o loop e capturar a próxima imagem

        cv2.waitKey(1)
