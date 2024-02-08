import hashlib
import random

g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

alice = random.getrandbits(256)
bob = random.getrandbits(256)
eve = random.getrandbits(256)

A = pow(g, alice, p)
E =pow(g, eve, p)
B = pow(g, bob, p)

s1 = pow(E, alice, p)
s2 = pow(A, eve, p)
s3 = pow(E, bob, p)
s4 = pow(B, eve, p)

if s1 == s2:
    s = hashlib.sha256(str(s1).encode()).hexdigest()
    print("Llave secreta: ", s)
else:
    print("Las llaves secretas no coinciden")

if s3 == s4:
    s = hashlib.sha256(str(s3).encode()).hexdigest()
    print("Llave secreta: ", s)
else:
    print("Las llaves secretas no coinciden")

if s4 == s1:
    s = hashlib.sha256(str(s1).encode()).hexdigest()
    print("Llave secreta: ", s)
else:
    print("Las llaves secretas no coinciden")