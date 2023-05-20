'''
Realizado en grupo por Mónica Inés Cesana Bernasconi, Nancy Cecilia Ojeda,
Juan Kiel Sodja Bogado, Emanuel Domingo Montenegro y Mario Luis	Fretes.

https://github.com/mfrettes/Informatorio2/edit/main/desafio4-grupo18.py
'''
def agregar_inmueble(lista_inmuebles):
    nuevo_inmueble = {}
    nuevo_inmueble['año'] = int(input("Año: "))
    nuevo_inmueble['metros'] = int(input("Metros cuadrados: "))
    nuevo_inmueble['habitaciones'] = int(input("Cantidad de habitaciones: "))
    nuevo_inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").upper() == "S"
    nuevo_inmueble['zona'] = input("Zona (A, B, C): ").upper()
    nuevo_inmueble['estado'] = input("Estado (Disponible, Reservado, Vendido): ").capitalize()

    if validar_inmueble(nuevo_inmueble):
        lista_inmuebles.append(nuevo_inmueble)
        guardar_inmuebles(lista_inmuebles)
        print("Inmueble agregado correctamente.")
    else:
        print("Error: El inmueble no cumple los requisitos mínimos.")


def editar_inmueble(lista_inmuebles):
    mostrar_inmuebles(lista_inmuebles)
    index = int(input("Ingrese el número del inmueble que desea editar: "))
    if index >= 0 and index < len(lista_inmuebles):
        inmueble = lista_inmuebles[index]

        while True:
            print("\nMenú de corrección:")
            print("1. Corregir año")
            print("2. Corregir metros")
            print("3. Corregir habitaciones")
            print("4. Corregir garaje")
            print("5. Corregir zona")
            print("6. Volver al menú principal")

            opcion_correccion = input("Ingrese su opción: ")
            if opcion_correccion == "1":
                nuevo_año = int(input("Ingrese el nuevo año: "))
                if nuevo_año >= 2000:
                    inmueble['año'] = nuevo_año
                    guardar_inmuebles(lista_inmuebles)
                    print("Año corregido correctamente.")
                else:
                    print("Error: El año debe ser igual o mayor a 2000.")
            elif opcion_correccion == "2":
                nuevo_metros = int(input("Ingrese los nuevos metros cuadrados: "))
                if nuevo_metros >= 60:
                    inmueble['metros'] = nuevo_metros
                    guardar_inmuebles(lista_inmuebles)
                    print("Metros cuadrados corregidos correctamente.")
                else:
                    print("Error: Los metros cuadrados deben ser igual o mayores a 60.")
            elif opcion_correccion == "3":
                nuevo_habitaciones = int(input("Ingrese la nueva cantidad de habitaciones: "))
                if nuevo_habitaciones >= 2:
                    inmueble['habitaciones'] = nuevo_habitaciones
                    guardar_inmuebles(lista_inmuebles)
                    print("Cantidad de habitaciones corregida correctamente.")
                else:
                    print("Error: La cantidad de habitaciones debe ser igual o mayor a 2.")
            elif opcion_correccion == "4":
                nuevo_garaje = input("¿Tiene garaje? (S/N): ").upper()
                if nuevo_garaje in ['S', 'N']:
                    inmueble['garaje'] = nuevo_garaje == "S"
                    guardar_inmuebles(lista_inmuebles)
                    print("Garaje corregido correctamente.")
                else:
                    print("Error: Opción inválida. Debe ingresar S para sí o N para no.")
            elif opcion_correccion == "5":
                nuevo_zona = input("Ingrese la nueva zona (A, B, C): ").upper()
                if nuevo_zona in ['A', 'B', 'C']:
                    inmueble['zona'] = nuevo_zona
                    guardar_inmuebles(lista_inmuebles)
                    print("Zona corregida correctamente.")
                else:
                    print("Error: Zona inválida. Debe ingresar A, B o C.")
            elif opcion_correccion == "6":
                print("Volviendo al menú principal.")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida del menú.")

    else:
        print("Error: Número de inmueble inválido.")


def eliminar_inmueble(lista_inmuebles):
    mostrar_inmuebles(lista_inmuebles)
    index = int(input("Ingrese el número del inmueble que desea eliminar: "))
    if index >= 0 and index < len(lista_inmuebles):
        inmueble = lista_inmuebles.pop(index)
        guardar_inmuebles(lista_inmuebles)
        print("Inmueble eliminado correctamente.")
    else:
        print("Error: Número de inmueble inválido.")


def validar_inmueble(inmueble):
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    return True


def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    zona = inmueble['zona']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio


def buscar_inmuebles_por_presupuesto(lista_inmuebles):
    presupuesto = float(input("Ingrese su presupuesto: "))

    inmuebles_encontrados = []
    for inmueble in lista_inmuebles:
        if inmueble['estado'] in ['Disponible', 'Reservado']:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble['precio'] = precio
                inmuebles_encontrados.append(inmueble)

    return inmuebles_encontrados


def mostrar_inmuebles(lista_inmuebles):
    for i, inmueble in enumerate(lista_inmuebles):
        print(f"Inmueble {i}:")
        print(f"Año: {inmueble['año']}")
        print(f"Metros cuadrados: {inmueble['metros']}")
        print(f"Habitaciones: {inmueble['habitaciones']}")
        print(f"Garaje: {'Sí' if inmueble['garaje'] else 'No'}")
        print(f"Zona: {inmueble['zona']}")
        print(f"Estado: {inmueble['estado']}")
        if 'precio' in inmueble:
            print(f"Precio: {inmueble['precio']}")
        print()


def guardar_inmuebles(lista_inmuebles):
    with open('inmuebles.txt', 'w') as archivo:
        for inmueble in lista_inmuebles:
            archivo.write(f"{inmueble}\n")


def cargar_inmuebles():
    try:
        with open('inmuebles.txt', 'r') as archivo:
            lineas = archivo.readlines()
            lista_inmuebles = [eval(linea) for linea in lineas]
            return lista_inmuebles
    except FileNotFoundError:
        return []


def mostrar_menu():
    print("\n***************Bienvenido a la Inmobiliaria XYZ")
    print('\n')
    print("1. Agregar, editar o eliminar inmuebles")
    print("2. Cambiar el estado de un inmueble")
    print("3. Búsqueda de inmuebles por presupuesto")
    print("4. Guardar y salir")


def modificar_estado_inmueble(lista_inmuebles):
    mostrar_inmuebles(lista_inmuebles)
    index = int(input("Ingrese el número del inmueble que desea modificar: "))
    if index >= 0 and index < len(lista_inmuebles):
        inmueble = lista_inmuebles[index]

        nuevo_estado = input(f"Ingrese el nuevo estado del inmueble (Disponible, Reservado, Vendido): ").capitalize()
        if nuevo_estado in ['Disponible', 'Reservado', 'Vendido']:
            inmueble['estado'] = nuevo_estado
            guardar_inmuebles(lista_inmuebles)
            print("Estado del inmueble modificado correctamente.")
        else:
            print("Error: Estado inválido. Debe ingresar Disponible, Reservado o Vendido.")
    else:
        print("Error: Número de inmueble inválido.")


lista_inmuebles = cargar_inmuebles()

while True:
    mostrar_menu()
    opcion = input("\nIngrese su opción: ")

    if opcion == "1":
        print("1. Agregar inmueble")
        print("2. Editar inmueble")
        print("3. Eliminar inmueble")

        subopcion = input("Ingrese su opción: ")

        if subopcion == "1":
            agregar_inmueble(lista_inmuebles)
        elif subopcion == "2":
            editar_inmueble(lista_inmuebles)
        elif subopcion == "3":
            eliminar_inmueble(lista_inmuebles)
        else:
            print("\nOpción inválida.")

    elif opcion == "2":
        modificar_estado_inmueble(lista_inmuebles)

    elif opcion == "3":
        inmuebles_encontrados = buscar_inmuebles_por_presupuesto(lista_inmuebles)
        print("\nInmuebles encontrados:")
        mostrar_inmuebles(inmuebles_encontrados)

    elif opcion == "4":
        print("\n¡Gracias por usar nuestro sistema!")
        break

    else:
        print("\nOpción inválida.")
