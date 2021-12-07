# Enunciado: un restaurante ofrece un descuento del 10% para consumo de hasta 100.00 y 
# un descuento del 20 % para consumos mayores, para ambos casos se aplica un impuesto del 19%. 
# Determinar el monto del descuento, el impuesto y el importe a pagar.
#
# Análisis: para la solución de este problema, se requiere que el usuario ingrese el consumo y 
# el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.
# monto del descuento
# impuesto
# importe a pagar

consumo = int(input("Ingrese su consumo: "))

impuesto = consumo*0.19
consumo += impuesto

if consumo < 100:
    monto = consumo*0.1
else:
    monto = consumo*0.2

consumo -= monto

print(f"Importe a pagar: {consumo}\nImpuesto: {impuesto}\nDescuento: {monto}")    


