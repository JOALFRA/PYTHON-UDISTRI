
import random
numero = []

while len (numero) < 3:
    digito = random.randint (0,9)
    if digito not in numero:
        numero.append (digito)

print (numero)

while True:
    intento = input ("INGRESE UN NÚMERO: ")

    usuario = []
    for i in intento:
        if int (i) not in usuario:
            usuario.append(int(i))

    if len (usuario) != len (numero):
        print ("INTENTO NO VALIDO: ")
    else:
        break

    print (usuario, numero)
