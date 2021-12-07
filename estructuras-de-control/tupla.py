# Una tupla consiste de un número de valores separados por comas

t = 12345, 54321, 'hello!'

print(t[0]) # Se puede acceder a cada valor mediante su indice como en un array
# Salida: 12345

print(t)
# Salida: (12345, 54321, 'hello!')

#Las tuplas puede ser anidadas
u = t, (1, 2, 3, 4, 5)
print(u)
#Salida: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Las tuplas son inmutables no se puede cambiar el valor de un indice.
# t[0] = 88888
# Salida:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# Pero puede contener objetos mutables como arrays
v = ([1, 2, 3], [3, 2, 1]) # Esta tupla contiene dos arrays
# Añadimos un valor más a el primer array de la tupla
v[0].append("Terry") 
print(v)
# Salida: ([1, 2, 3, 'Terry'], [3, 2, 1])

# Se puede contar la cantidad de objetos de una tupla mediante len()
print(len(t))
# Salida: 3


