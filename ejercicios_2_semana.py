#  1. Escribe un programa que pide al usuario su edad y muestre 
#  por pantalla si es mayor de #edad (18 o más))o no.

edad= int(input("Ingrese su edad:  "))

if edad >= 18:
     print(f"Usted tiene {edad} años, por ello es mayor de edad ")
else:
     print(f"Usted tiene {edad} años, por ello es menor de edad ")

#  2-Escribir un programa que pida al usuario un número entero y muestre por
#  pantalla si es positivo, negativo o cero.

numero = int(input("Introduce un número entero: "))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")

#  3-Escribir un programa que pida al usuario dos números y muestre por pantalla
#  cuál de ellos es mayor.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num1 > num2:
    print("El primer número es mayor")
elif num2 > num1:
    print("El segundo número es mayor")
else:
    print("Ambos números son iguales")

#  4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
#  pantalla si está aprobado (5 o más) o no.

nota = float(input("Introduce tu nota: "))
if nota >= 5:
    print("¡Felicidades! Has aprobado")
else:
    print("Lo siento, no aprobaste")

#  5-Escribir un programa que pida al usuario un número entero y muestre por
#  pantalla si es par o impar.

numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#  6-Escribir un programa que pida al usuario un número entero y muestre por
#  pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Introduce un número entero: "))
if numero % 2 == 0 and numero % 3 == 0:
    print("El número es múltiplo de 2 y de 3")
else:
    print("El número no es múltiplo de 2 y de 3 a la vez")

#  7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
#  es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input("Introduce un carácter: ")
if caracter.isupper():
    print("Es una letra mayúscula")
elif caracter.islower():
    print("Es una letra minúscula")
elif caracter.isdigit():
    print("Es un número")
else:
    print("Es un carácter especial")

#  8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
#  por pantalla si contiene la letra "a".

cadena = input("Introduce una cadena de caracteres: ")
if "a" in cadena:
    print('La cadena contiene la letra \"a\" ')
else:
    print('La cadena no contiene la letra \"a\" ')

#  9-Escribir un programa que pida al usuario tres números y muestre por pantalla
#  el mayor de ellos.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"El primer número: {num1}, es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"El segundo número: {num2}, es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"El tercer número: {num3}, es el mayor")
else:
    print("Los tres números son iguales")

#  9.1 -Escribir un programa que pida al usuario tres números y muestre por pantalla
#  el mayor de ellos. Redondeo con 2 decimales usando la función round(valor,n) 

num1 = round(float(input("Introduce el primer número: ")),2)
num2 = round(float(input("Introduce el segundo número: ")),2)
num3 = round(float(input("Introduce el tercer número: ")),2)

if num1 > num2 and num1 > num3:
    print(f"El primer número: {num1}, es el mayor")
elif num2 > num1 and num2 > num3:
    print(f"El segundo número: {num2}, es el mayor")
elif num3 > num1 and num3 > num2:
    print(f"El tercer número: {num3}, es el mayor")
else:
    print("Los tres números son iguales")

#  10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
#  una vocal o una consonante.
'''
Este código en Python solicita al usuario que introduzca una letra por medio de la 
función `input`, y luego procesa la entrada del usuario para determinar si la letra 
ingresada es una vocal o una consonante.

En la línea `if letra.lower() in ("a", "e", "i", "o", "u")`, se verifica si la letra 
ingresada por el usuario está en la tupla (`tuple`) de vocales 
("a", "e", "i", "o", "u"). El uso del método `.lower()` convierte a minúsculas 
la letra ingresada por el usuario antes de verificar su presencia en la 
tupla de vocales. Si la letra ingresada se encuentra en la tupla de vocales, 
se imprime en pantalla el mensaje "La letra introducida es una vocal". 
De lo contrario, se imprime el mensaje "La letra introducida es una consonante".

'''

letra = input("Introduce una letra: ")
if letra.lower() in ("a", "e", "i", "o", "u"):
    print("La letra introducida es una vocal")
else:
    print("La letra introducida es una consonante")

#  11-Escribir un programa que pida al usuario dos números y muestre por pantalla
#  la suma de ellos solo si ambos son pares.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("La suma de los dos números es", num1 + num2)
else:
    print("Ambos números no son pares, no se pueden sumar")
