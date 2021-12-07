# Los diccionarios son como los arrays asociativos en otros lenguajes
# Se crean con llaves. Se puede isnertar y extraer datos y elimintarlos con del.
# Tambien se puedne listar  las claves con list(d) y de forma ordenada con sorted(d)
# Para comprobar si una clave está en el diccionario usa la palabra clave in.

# Creamos un diccionario
tel = {'jack': 4098, 'sape': 4139}
# Añadimos una nueva clave:valor al diccionario
tel['guido'] = 4127

print(tel)
# Salida: {'jack': 4098, 'sape': 4139, 'guido': 4127}

# Mostrar valor por indicando su clave
print(tel['jack'])
# Salida: 4098

#Borrar un dato
del tel['sape']

# Añadimos una nueva clave:valor al diccionario
tel['irv'] = 4127

print(tel)
# Salida: {'jack': 4098, 'guido': 4127, 'irv': 4127}

# Listar claves por orden en diccionario
print(list(tel))
# Salida: ['jack', 'guido', 'irv']

# Listar claves por orden alfabetico
print(sorted(tel))
# Salida: ['guido', 'irv', 'jack']

# Funcionamiento de la palabra clave in en los diccionarios
print('guido' in tel)
# Salida: True
print('jack' not in tel)
# Salida: False