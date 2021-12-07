from math import sqrt

print("Dados los catetos calcular la hipotenusa")

#Entrada de datos
cat1 = float(input("Cateto 1: "))
cat2 = float(input("Cateto 2: "))

#Operacion con math
hipotenusa1 = round((sqrt(cat1**2+cat2**2)), 2)

#Operacion sin math
hipotenusa2 = round(((cat1**2+cat2**2)**0.5), 2)

#Resultado
print(f"Hipotenusa con math: {hipotenusa1}\nHipotenusa sin math: {hipotenusa2}")
