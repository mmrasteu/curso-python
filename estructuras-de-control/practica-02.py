# Enunciado: debido a los excelentes resultados, el restaurante decide ampliar sus ofertas de acuerdo 
# a la siguiente escala de consumo, ver la tabla. 
# Determinar el monto del descuento, el importe del impuesto y el importe a pagar.
# 
# Consumo (S/.)   Descuento (%)
# Hasta 100       10
# Mayor a 100     20
# Mayor a 200     30
# 
# Análisis: para la solución de este problema, se requiere que el usuario ingrese el consumo y el 
# sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.

consumo = int(input("Ingrese su consumo: "))

impuesto = consumo*0.19
consumo += impuesto

if consumo < 100:
    monto = consumo*0.1
elif consumo < 200:
    monto = consumo*0.2
else:
    monto = consumo*0.3

consumo -= monto

print(f"Importe a pagar: {consumo}\nImpuesto: {impuesto}\nDescuento: {monto}")    


