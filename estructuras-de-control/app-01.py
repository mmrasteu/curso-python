#Detectar si el numero ingresado es un par positivo, par negativo, impar positivo, impar negativo o 0

num = int(input("Introduce un numero: "))
salida = "El numero es "

# Dejar un if vacio
# if condition:
#    pass    <-- pass es una palabra reservada para indicar que no se hará nada en este bloque


if num > 0:
    salida += "positivo "
    if num%2 == 0:
        salida += "par"
    else:
        salida += "impar"
elif num < 0:
    salida += "negativo "
    if num%2 == 0:
        salida += "par"
    else:
        salida += "impar"
else:
    salida += "0"
    
print(f"{salida}")


