# También es posible usar una lista como una cola, donde el primer elemento añadido es el primer elemento retirado 
# («primero en entrar, primero en salir» FIFO); 
# sin embargo, las listas no son eficientes para este propósito. 
# Agregar y sacar del final de la lista es rápido, pero insertar o sacar del comienzo de una lista es lento 
# (porque todos los otros elementos tienen que ser desplazados por uno).

# Para implementar una cola, utiliza collections.deque el cual fue diseñado para añadir y quitar de ambas 
# puntas de forma rápida.

from collections import deque

cola = deque(["Eric", "John", "Michael"])

cola.append("Terry")    # Introducimos a Terry en cola
cola.append("Graham")   # Introducimos a Graham en la cola

# Mostramos la cola actual
print(cola) 
# Salida: deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

# El primero en entrar, Eric, será el primero en salir.
print(cola.popleft()) 

# Ahora el primero es John y será el primero en salir.
print(cola.popleft()) 

# Mostramos lo que queda de cola.
print(cola) 
# Salida: deque(['Michael', 'Terry', 'Graham'])
