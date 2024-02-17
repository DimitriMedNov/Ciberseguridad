from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generar las llaves RSA de Alice
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

# Genera un HASH h(M) del mensaje
mensaje = b"Este es el mensaje de Alice."
digest = hashes.Hash(hashes.SHA256())
digest.update(mensaje)
hash_mensaje = digest.finalize()

# Alice firma el HASH h(M) con su llave privada
firma = private_key.sign(
    hash_mensaje,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Bob verifica la firma con la llave pública de Alice
try:
    public_key.verify(
        firma,
        hash_mensaje,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("La firma es válida. El mensaje es auténtico.")
except Exception as e:
    print("La firma no es válida. El mensaje no es auténtico.")

