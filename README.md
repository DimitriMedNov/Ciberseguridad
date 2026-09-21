# Prácticas de ciberseguridad

Prácticas de la materia de ciberseguridad de la Universidad Anáhuac Mayab, en Python.

## Qué hay

| Archivo | Qué demuestra |
|---|---|
| `PracticaHASH.py` | Funciones hash y para qué sirve que sean de un solo sentido |
| `RSA.py` | Cifrado asimétrico con llave pública y privada |
| `TestFirmaAlice.py` | Firma digital: cómo se comprueba quién firmó |
| `Deffie_Hellman.py` | Ponerse de acuerdo en una llave compartida sin enviarla nunca |
| `AtaqueMitMProtocoloDiffieHellman.py` | Por qué ese acuerdo se rompe si alguien se mete en medio |
| `Fernet.py` · `Desencriptado.py` | Cifrado simétrico con una llave de sesión |

El del ataque de hombre en medio es el más interesante de los seis: muestra que Diffie-Hellman protege el secreto pero no dice con quién estás hablando, que es justo lo que resuelven los certificados.

## Stack

Python · cryptography · PyCryptodome
