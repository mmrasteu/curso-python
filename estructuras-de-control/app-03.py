# Obtener la suma de los primeros N número natural positivo.
#
# Para la solución de este problema, se requiere que el usuario ingrese un número 
# y el sistema realice el proceso para devolver la suma de los N primeros números.

n = int(input("Ingrese un numero: "))

suma = 0
count = 0
while count  < n: 
    suma += count
    count += 1
    
print(suma)