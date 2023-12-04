import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

leitor = SimpleMFRC522()

data = "8504312"

print("Aproxime a TAG do leitor para gravar")

leitor.write(data)
print("Concluído!")
