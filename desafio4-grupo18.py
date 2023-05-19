#otro ejemplo, usando funciones, del desafío 4: "La Inmobiliaria"
#Lista de inmuebles
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
             {'año': 2016, 'metros': 80, 'aciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
             {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
             {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
             {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

# Función para agregar un nuevo inmueble a la lista
def agregar_inmueble(inmuebles, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble): # Verificar que el inmueble cumple las reglas de validación
        inmuebles.append(nuevo_inmueble)
        print("Inmueble agregado con éxito")
    else:
        print("El inmueble no cumple las reglas de validación")

# Función para editar un inmueble existente en la lista
def editar_inmueble(inmuebles, indice, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble): # Verificar que el inmueble cumple las reglas de validación
        inmuebles[indice] = nuevo_inmueble
        print("Inmueble editado con éxito")
    else:
        print("El inmueble no cumple las reglas de validación")

# Función para eliminar un inmueble existente de la lista
def eliminar_inmueble(inmuebles, indice):
    del inmuebles[indice]
    print("Inmueble eliminado con éxito")

# Función para cambiar el estado de un inmueble existente en la lista
def cambiar_estado(inmuebles, indice, nuevo_estado):
    inmuebles[indice]['estado'] = nuevo_estado
    print("Estado de inmueble modificado con éxito")

# Función para buscar inmuebles según un presupuesto dado
def buscar_inmuebles(inmuebles, presupuesto):
    inmuebles_encontrados = []
    for inmueble in inmuebles:
        if inmueble['estado'] in ['Disponible', 'Reservado'] and inmueble['año'] >= 2000 and inmueble['metros'] >= 60 and inmueble['habitaciones'] >= 2 and inmueble['zona'] in ['A', 'B', 'C']:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

# Función para validar si un inmueble cumple las reglas de validación
def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] <2:
        return False
    return True

# Función para calcular el precio de un inmueble según la zona
def calcular_precio(inmueble):
    if inmueble['zona'] == 'A':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1 - (2021 - inmueble['año']) / 100)
    elif inmueble['zona'] == 'B':
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1000) * (1 - (2021 - inmueble['año']) / 100)
    else:
        precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 500) * (1 - (2021 - inmueble['año']) / 100)
    return precio                                                                                                                       
