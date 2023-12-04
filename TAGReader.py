import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

print("Aproxime a TAG do leitor para realizar a leitura!")

while True:
    id, texto = leitor.read()
    print("ID: {}\nTexto: {}".format(id, texto))
    sleep(3)
