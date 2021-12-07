# Crea 2 listas y una tupla que tendrá números de 1 a 9. 
# La primera lista se llamará pares y el segundo impar, ambos estarán vacíos. 
# Después multiplica cada uno de los números de la tupla por un número aleatorio entre 1 y 100, 
# si el resultado es par guarda ese número en la lista de pares y si es impar en la lista  de impares. 
# Muestra por consola: -la multiplicación que se produce junto con su resultado con el formato 2 x 3 = 6 
# y la lista de pares e impares
import random

pares = []
impar = []

t = 1,2,3,4,5,6,7,8,9

c = 0

while c < len(t):
    n = random.randint(1, 100) * t[c]
    
    if n%2 == 0:
        pares.append(n)
    else:
        impar.append(n)
        
    c += 1
    
print(f"Lista de numeros pares: {pares}\nLista de numeros impares: {impar}")
