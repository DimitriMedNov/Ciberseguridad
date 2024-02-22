import hashlib

def calcular_hash_texto(texto):
    hash_objeto = hashlib.sha256(texto.encode())
    return hash_objeto.hexdigest()

texto = 'ABCDEFGH'
hash_texto = calcular_hash_texto(texto)
print('HASH 8 Bits: '.ljust(30), hash_texto)

def calcular_hash_texto_largo(texto):
    hash_objeto = hashlib.sha256(texto.encode())
    return hash_objeto.hexdigest()

# Ejemplo de uso para una cadena de texto
texto_largo = 'Esta es una cadena de texto más larga'
hash_texto_largo = calcular_hash_texto_largo(texto_largo)
print('HASH 1024 Bits: '.ljust(30),hash_texto_largo)

def calcular_hash_archivo(ruta_archivo, algoritmo='sha256'):
    hash_objeto = hashlib.new(algoritmo)
    try:
        # Leer el archivo en modo binario
        with open(ruta_archivo, "rb") as archivo:
            # Leer y actualizar el hash en bloques de 4K
            for bloque in iter(lambda: archivo.read(4096), b""):
                hash_objeto.update(bloque)
    except FileNotFoundError:
        return "El archivo no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"

    # Devolver el hash en hexadecimal
    return hash_objeto.hexdigest()

# Ruta completa al archivo PDF
ruta_completa_pdf = r'C:\Users\MedNo\OneDrive\Escritorio\Tareas\Activity_Session_8_EF_IMATRIX.pdf'

# Calcular y mostrar el hash del archivo PDF
hash_del_pdf = calcular_hash_archivo(ruta_completa_pdf)
print('HASH de un archivo PDF: '.ljust(30),hash_del_pdf)

