# CALCULADORA SENCILLA_PHYTON
#
# Función para realizar suma
def sumar(num1, num2):
    return num1 + num2

# Función para realizar resta
def restar(num1, num2):
    return num1 - num2

# Función para realizar multiplicación
def multiplicar(num1, num2):
    return num1 * num2

# Función para realizar división
def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return num1 / num2


# Mostramos el menú de opciones al usuario
print("Calculadora sencilla:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

# Pedimos al usuario que seleccione una opción
opcion = int(input("Ingrese su opción (1/2/3/4): "))

# Pedimos al usuario los números a operar
num1 = float(input("Ingrese el primer número: "))

num2 = float(input("Ingrese el segundo número: "))

# Realizamos la operación seleccionada por el usuario
if opcion == 1:
    resultado = sumar(num1, num2)
elif opcion == 2:
    resultado = restar(num1, num2)
elif opcion == 3:
    resultado = multiplicar(num1, num2)
elif opcion == 4:
    resultado = dividir(num1, num2)
else:
    print("Opción inválida")
    resultado = None

# Mostramos el resultado de la operación si no hubo errores
if resultado is not None:
    print(f"El resultado es: {resultado}")
   