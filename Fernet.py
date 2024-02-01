#cifrado Fernet

#importamos fernet
from cryptography.fernet import Fernet

#Generamos la clave
clave = Fernet.generate_key()

#creamos la instancia de fernet
f = Fernet(clave)

print(clave)

#encriptamos el mensaje
token =  f.encrypt(b'Adolf Hitler, quien fue el lider del Partido Nazi y Canciller de Alemania '
                   b'desde 1933 hasta 1945, es una figura historica conocida principalmente '
                   b'por su papel en la instigacion de la Segunda Guerra Mundial y los horrores '
                   b'del Holocausto. '
                   b'Hi Hitler!')

#mensaje cifrado
print(token)

#descifrar
des = f.decrypt(token)

#descifrado
print(des)