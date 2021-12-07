# En una pila el último dato en ingresar será el primer dato en salir
# Con los metodos stack() para ignresar y pop() para sacar podemos crear pilas

stack = [3, 4, 5]
print(stack)

#Añadimos datos nuevos
stack.append(6) # [3, 4, 5, 6]
stack.append(7) # [3, 4, 5, 6, 7]
print(stack)

#Sacamos datos
print(stack.pop()) # 7
print(stack)       # [3, 4, 5, 6]

print(stack.pop()) # 6
print(stack)       # [3, 4, 5]

print(stack.pop()) # 5
print(stack)       # [3, 4]