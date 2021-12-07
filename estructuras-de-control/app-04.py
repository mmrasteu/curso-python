# Obtén todos lo elementos de una lista usando for loop y while loop
#
# Para solucionar este problema se requiere una lista con elementos 
# e iterar cada uno des sud elementos como una lista.

datos = ["Miguel", "Angel", 10, 1.67, True]

for dato in datos: 
    print(dato)
    
#Se puede hacer con while
c = 0
while c < len(datos):
    print(datos[c])
    c += 1
    
for n in range(0, 10):
    print(n)