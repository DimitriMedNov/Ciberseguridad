from Crypto.Util.number import getPrime, inverse
from Crypto.Random import get_random_bytes
import Crypto.Util.number
import hashlib

# Número de bits
bits = 1024

# Obtener los primos para Alice
pA = getPrime(bits, randfunc=get_random_bytes)
qA = getPrime(bits, randfunc=get_random_bytes)

# Calcular n (parte de la llave pública) y phi (para la llave privada) de Alice
nA = pA * qA
phiA = (pA - 1) * (qA - 1)

# Clave pública (e, nA)
e = 65537

# Calcular la llave privada de Alice
dA = inverse(e, phiA)

# Función para firmar un mensaje con la clave privada de Alice
def sign(message, d, n):
    # Convertir el mensaje en un entero basado en su hash SHA-256
    hash = int.from_bytes(hashlib.sha256(message.encode('utf-8')).digest(), byteorder='big')
    # Crear la firma utilizando la clave privada de Alice (dA)
    signature = pow(hash, d, n)
    return signature

# Función para verificar una firma con la clave pública de Alice
def verify(message, signature, e, n):
    # Convertir el mensaje en un entero basado en su hash SHA-256
    hash = int.from_bytes(hashlib.sha256(message.encode('utf-8')).digest(), byteorder='big')
    # Desencriptar la firma con la clave pública
    hash_from_signature = pow(signature, e, n)
    # Comparar el hash del mensaje con el hash desencriptado de la firma
    return hash == hash_from_signature

# Alice firma un mensaje
msg = "Hola Mundo"
signature = sign(msg, dA, nA)
print("Firma: ", signature, "\n")

# Bob verifica la firma
verification = verify(msg, signature, e, nA)
print("Verificación: ", verification, "\n")

# Si la verificación es True, la firma es válida. Si es False, la firma es inválida.
