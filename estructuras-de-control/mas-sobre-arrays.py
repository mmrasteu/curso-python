#Más sobre arrays o listas

datos = ["Miguel", "Angel"]
print(datos)

# Agrega un ítem al final de la lista
datos.append(28)
print(datos)

# Agrega un array a otro.
datos_extra = ["Cadiz", "España"]
datos.extend(datos_extra)
print(datos)

# Inserta un ítem en una posición dada. El primer argumento es el índice del ítem delante del cual se insertará
# Se agregará delante de Cadiz
datos.insert(3, "El Puerto de Santa Maria")
print(datos)

# Quita el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.
datos.remove("España")
print(datos)

# Quita el ítem en la posición dada de la lista y lo retorna. 
# Si no se especifica un índice, a.pop() quita y retorna el último elemento de la lista.
dato_popeado = datos.pop(4)
print(datos)
print(dato_popeado)

# Retorna el índice basado en cero del primer elemento cuyo valor sea igual a x. 
# Lanza una excepción ValueError si no existe tal elemento.
print(datos.index("Miguel"))
# Podemos indicar un rango de busqueda
print(datos.index("Angel", 0, 2))

# Retorna el número de veces que x aparece en la lista.
datos_repetitivos = ["Cadiz", "Cadiz", "Cadiz", "Cadiz", "Cadiz", "Sevilla"]
print(datos_repetitivos.count("Cadiz"))
print(datos_repetitivos.count("Sevilla"))

# Ordena los elementos de la lista in situ
datos_desordenados = ["B", "D", "C", "A"]
print(datos_desordenados)
datos_desordenados.sort()
print(datos_desordenados) # Ahora ordenados

# Invierte los elementos de la lista in situ.
datos_desordenados.reverse()
print(datos_desordenados) # Ahora invertidos

# Retorna una copia superficial de la lista.
print(datos_desordenados.copy()) 

#Elimina todos los elementos de la lista. 
datos_desordenados.clear()
print(datos_desordenados) # Lista vacía