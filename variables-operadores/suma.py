print('Suma de dos numeros enteros')

#Entrada de datos en variable 'a' usando input() para pedir datos por teclado
#Si no indicamos el tipo de dato, input() lo considerará un string
#Para hacer la conversion de datos o casting de datos usaremos diferentes funciones

#Convertir a tipo int con int(). Para float float(). Para string str().
a = int(input('Ingrese primer numero: '))
b = int(input('Ingrese segundo numero: '))

#Operacion de suma y almacenar en variable 'suma'
suma = a+b

#Salida
print(f'La suma es: {suma}')