# 1. Solicitar nombre al usuario y mostrar en pantalla:

nombre = input("Ingrese su nombre: ")
print(f"Su nombre es {nombre}")


# 2. Solicitar nombre al usuario y mostrar un mensaje de bienvenida:

nombre = input("Ingrese su nombre: ")
print(f"Bienvenido/a {nombre}!")


# 3. Solicitar edad al usuario y mostrar en pantalla:

edad = int(input("Ingrese su edad: "))
print(f"Usted tiene {edad} años")


# 4. Calcular la suma de dos números ingresados por el usuario y mostrar en pantalla:

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}")


# 5. Mostrar el cociente y resto de la división de dos números enteros ingresados por el usuario:

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
cociente = num1 // num2
resto = num1 % num2
print(f"El cociente de la división es {cociente}")
print(f"El resto de la división es {resto}")


# 6. Calcular el área de un círculo a partir del radio:

pi = 3.1416
radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio ** 2
print(f"El área del círculo es {area}")


# 7. Calcular el área de un triángulo utilizando base y altura:

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print(f"El área del triángulo es {area}")


# 8. Calcular diámetro, circunferencia y área de un círculo a partir del radio:

pi = 3.14159
radio = float(input("Ingrese el radio del círculo: "))
diametro = radio * 2
circunferencia = 2 * pi * radio
area = pi * radio ** 2
print(f"El diámetro del círculo es {diametro}")
print(f"La circunferencia del círculo es {circunferencia}")
print(f"El área del círculo es {area}")


# 9. Realizar operaciones matemáticas básicas con dos números ingresados por el usuario 
#    y mostrar en pantalla:

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print(f"La suma es {num1 + num2}")
print(f"La resta es {num1 - num2}")
print(f"El producto es {num1 * num2}")
print(f"La división es {num1 / num2}")


# 10. Convertir dólares a euros:

tipo_cambio = 0.90
dolares = float(input("Ingrese el monto en dólares: "))
euros = dolares * tipo_cambio
print(f"{dolares} dólares equivalen a {euros} euros")


# 11. Contar la cantidad de letras en una palabra ingresada por el usuario:

palabra = input("Ingrese una palabra: ")
cantidad_letras = len(palabra)
print(f"La palabra ingresada tiene {cantidad_letras} letras")


# 12. Calcular la edad de una persona a partir de su fecha de nacimiento:

fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
dia, mes, ano = fecha_nacimiento.split("/")
edad = 2023 - int(ano)
print(f"Usted tiene {edad} años")

#   12.1 Calculo la edad de una persona a partir de su fecha de nacimiento y año ingresado

print("Calculo la edad de una persona a partir de su fecha de nacimiento y año ingresado ")
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
ano_actual = input("Ingrese año actual o tentativo para calcular la edad:  ")
dia, mes, ano = fecha_nacimiento.split("/")
edad = int(ano_actual) - int(ano)
print(f"Usted tiene {edad} años")


# 13. Calcular la edad de una persona en 10 años más a partir de su edad actual:

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad_en_10_anos = edad + 10
print(f"En 10 años usted tendrá {edad_en_10_anos} años, {nombre}")


# 14. Mostrar el doble y triple de un número ingresado por el usuario:

numero = int(input("Ingrese un número entero: "))
print(f"El doble de {numero} es {numero * 2}")
print(f"El triple de {numero} es {numero * 3}")


# 15. Convertir temperatura en grados Celsius a grados Fahrenheit:

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")


# 16. Calcular el índice de masa corporal a partir del peso y altura ingresados por el usuario:

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura ** 2
print(f"Su índice de masa corporal es {imc:.2f}")


# 17. Mostrar dos palabras en orden inverso:

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")
print(f"{palabra2} {palabra1}")


# 18. Mostrar nombre, edad y ciudad de residencia en una sola línea:

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad de residencia: ")
print(f"{nombre}, {edad} años, residente en {ciudad}")


# 19-Escribe un programa que solicite al usuario un número decimal y luego
#    imprima la parte entera y decimal por separado.

numero = float(input("Ingrese un número decimal: ")) 
parte_entera = int(numero) 
parte_decimal = numero - parte_entera 
print(f"La parte entera es {parte_entera}") 
print(f"La parte decimal es {parte_decimal}")

# 19.1- Escribe un programa que solicita al usuario un número decimal y luego
# imprime la parte entera y decimal por separado, redondeando con la
# función round(x,n) para redondear y limitar a "n" decimales.

numero = float(input("Ingrese un número decimal: ")) 
parte_entera = int(numero) 
parte_decimal = round((numero - parte_entera),2) 
print(f"\nLa parte entera es {parte_entera}") 
print(f"La parte decimal es {parte_decimal}")


# DESAFIOS 
#  -----------------------------------------------------------------------------
# 1. Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su
# nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto
# que le corresponde por las comisiones
# Pedimos el nombre del vendedor y su venta total en el mes

nombre = input("Ingrese su nombre: ")
venta_total = float(input("Ingrese su venta total en el mes: "))

# Calculamos la comisión del 6% de la venta total
comision = venta_total * 0.06

# Mostramos un mensaje con su nombre y la comisión que le corresponde
print(f"Hola {nombre}, su comisión correspondiente al 6% de su venta \
     total de ${venta_total:.2f} es de ${comision:.2f}. ¡Felicitaciones!")

#-------------------------------------------------------------------
''' 
Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:
La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono]
'''

#  2.-Pidiéndole al usuario su información personal
nombre = input("Ingrese su nombre completo: ")
edad = input("Ingrese su edad: ")
estatura = input("Ingrese su estatura en cm: ")
peso = input("Ingrese su peso en kg: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

# Imprimiendo los datos ingresados por el usuario utilizando el formato especificado
print("La información ingresada es la siguiente:")
print("Nombre completo: {}".format(nombre))
print("Edad: {}".format(edad))
print("Estatura: {} cm".format(estatura))
print("Peso: {} kg".format(peso))
print("Dirección: {}".format(direccion))
print("Número de teléfono: {}".format(telefono))
