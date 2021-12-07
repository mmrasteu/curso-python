#Bucle con else, break y continue

c = 0

while c < 10:
    c+=1
    print(c)
    
    # Si se cumple el if no pasa por el else porque salta el break y sale dle bucle
    # if c == 5:
    #     print("Termina el bucle")
    #     break
    
    # Si se cumple el if saltará a la siguiente iteracion por el continue
    if c == 5:
        print("Salta a la siguiente iteracion")
        continue
    # todo lo que venga debajo de continue nos e ejecutará en esa iteracion
    
    print("Despues del continue")
    
else:
    print("Fin de while")


    