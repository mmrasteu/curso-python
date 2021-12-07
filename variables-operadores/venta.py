print("Dado el valor base de un producto se mostrará su IVA (del 19%) y su precio de venta")

#Tomar valores
valor = float(input("Precio del producto: "))

#Operaciones
iva = round(valor * 0.19 , 2)
precio = round(valor + iva , 2)

#Imprimir resultados

print(f"Iva: {iva}. Precio venta: {precio}")