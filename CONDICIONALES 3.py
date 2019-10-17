
numero = int (input("INGRESE UN NÚMERO A VALIDAR: "))

dias = ["DOMINGO", "LUNES","MARTES","MIÉRCOLES","JUEVES","VIERNES","SÁBADO"]

if numero < 1 or numero > 7:
    print ("EL NÚMERO NO ES UN DÍA VALIDO")

else:
    print ("EL NÚMERO CORRESPONDE A: " + dias [numero -1])
