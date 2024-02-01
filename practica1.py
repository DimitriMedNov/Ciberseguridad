from Crypto.Util import number
import random
print("-----------------------------Ejercicio 1-----------------------------------------------")
#Ejercicio 1
print('\n', "Ejercicio 1 - Obtener un num aleatorio de 256 bits usando la funcion random",
'\n', '\n', random.getrandbits(256), '\n')


print("----------------------------------Ejercicio 2------------------------------------------")
#Ejercicio 2 obtener num aleatorio primo
i = 0
while(True):
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if(esPrimo):
        print("En la iteración:", i, "se econtró el primo", j, "\n")
        break

print("-------------------------------Ejercicio 3---------------------------------------------")
#ejercicio 3 Inversio  multiplicativo
def inversMultiplicativo(x,y):
    print("Ejercicio3 - El inverso multiplicativo del numero x:, ", "\n", x, "\n", "y el numero y: ", "\n", "es: ", "\n", number.inverse(x,y), "\n")

a = random.getrandbits(1024)
b = random.getrandbits(1024)

inversMultiplicativo(a,b)

print("-------------------------------Ejercicio 4---------------------------------------------")
#ejercicio 4 Metodos de cifrado
#encontrar la potencia de un numero 2^(e) mod p, donde "e" es un numero de 256 bits y "p" es un primo de 1024 bits

a = 2
b = random.getrandbits(256)
c = j

def potencial(x,y,z):
    print("Ejercicio 4 - la potencia de x a la y mod z es: ", "\n", pow(x,y,z), "\n")

potencial(a,b,c)