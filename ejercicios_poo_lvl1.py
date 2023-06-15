'''
Ejercicio 1: Vehículo pt.1
------------------------------
Existe un diagrama que muestra un rectángulo con nombre Vehículo con dos atributos:
Color y Ruedas. Hay otro rectángulo del cual sale una flecha hacia Vehículo y que tiene
como nombre: Coche, con dos atributos: Velocidad (km/h) y Cilindrada (cc). 
A partir del siguiente diagrama de clases, implementá
clases y métodos para mostrar atributos.
'''
'''
Primero, creamos la clase Vehiculo con los atributos de color y ruedas:
'''
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
'''
Luego, creamos la clase Coche que hereda de Vehiculo y define los atributos de velocidad
y cilindrada:
'''
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
'''
Por último, definimos los métodos para mostrar los atributos de cada clase:
'''
class Vehiculo:
    # ...definición de atributos
    def mostrar_atributos(self):
        print(f"Color: {self.color}")
        print(f"Ruedas: {self.ruedas}")

class Coche(Vehiculo):
    # ...definición de atributos
    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Cilindrada: {self.cilindrada} cc")

'''
Con esta implementación, podemos crear objetos de ambas clases y usar el 
método mostrar_atributos() para mostrar sus atributos:
'''
# Crear un objeto de la clase Vehiculo
vehiculo = Vehiculo("rojo", 4)
vehiculo.mostrar_atributos()

# Crear un objeto de la clase Coche
coche = Coche("azul", 4, 120, 2000)
coche.mostrar_atributos()

'''
La salida para la llamada a mostrar_atributos() de vehiculo sería:

Color: rojo
Ruedas: 4

Mientras que la salida para la llamada a mostrar_atributos() de coche sería:

Color: azul
Ruedas: 4
Velocidad: 120 km/h
Cilindrada: 2000 cc
'''

'''
Ejercicio 2: Vehículo pt2. 
-----------------------------------
Hay un listado de nombre Vehículos con dos atributos: Color y Ruedas. Contiene otros vehículos
como ser: Coche (Velocidad: km/h, Cilindrada: cc), Camioneta (carga en kg), 
Bicicleta (Tipo urbana/deportiva) y Motocicleta (Velocidad: km/h, Cilindrada: cc). 
Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
mostrando el nombre de su clase y sus atributos.
Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que 
muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} 
ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 
ruedas como valor.
'''
'''
Primero, definimos la clase Vehiculo con los atributos de color y ruedas:
'''
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

'''
Luego, definimos las clases hijas que heredan de la clase Vehiculo:
'''
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

'''
Luego, creamos al menos un objeto de cada subclase y los
añadimos a una lista llamada vehiculos:
'''
coche = Coche("rojo", 4, 120, 2000)
camioneta = Camioneta("negra", 4, 1000)
bicicleta = Bicicleta("verde", 2, "urbana")
motocicleta = Motocicleta("azul", 2, 180, 600)
vehiculos = [coche, camioneta, bicicleta, motocicleta]

'''
Luego, definimos la función catalogar que recorre la lista de vehículos y muestra el nombre
de su clase y sus atributos.
Si se le pasa un argumento ruedas, solo muestra los vehículos con ese número de ruedas:
'''
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos = [v for v in vehiculos if v.ruedas == ruedas]
        print("Se han encontrado {} vehículos con {} ruedas:".format(len(vehiculos), ruedas))
    for vehiculo in vehiculos:
        nombre = type(vehiculo).__name__
        atributos = vars(vehiculo)
        print("{}: {}".format(nombre, atributos))

'''
Por último, podemos probar la función catalogar con varios argumentos para ver los 
resultados:
'''

# Mostrar todos los vehículos
catalogar(vehiculos)

# Mostrar los vehículos con 2 ruedas
catalogar(vehiculos, ruedas=2)

# Mostrar los vehículos con 4 ruedas
catalogar(vehiculos, ruedas=4)

# Mostrar los vehículos con 0 ruedas (no hay ninguno)
catalogar(vehiculos, ruedas=0)

'''
La salida para las llamadas de catalogar anteriores sería la siguiente:

Coche: {'color': 'rojo', 'ruedas': 4, 'velocidad': 120, 'cilindrada': 2000}
Camioneta: {'color': 'negra', 'ruedas': 4, 'carga': 1000}
Bicicleta: {'color': 'verde', 'ruedas': 2, 'tipo': 'urbana'}
Motocicleta: {'color': 'azul', 'ruedas': 2, 'velocidad': 180, 'cilindrada': 600}
Se han encontrado 2 vehículos con 2 ruedas:
Bicicleta: {'color': 'verde', 'ruedas': 2, 'tipo': 'urbana'}
Motocicleta: {'color': 'azul', 'ruedas': 2, 'velocidad': 180, 'cilindrada': 600}
Se han encontrado 2 vehículos con 4 ruedas:
Coche: {'color': 'rojo', 'ruedas': 4, 'velocidad': 120, 'cilindrada': 2000}
Camioneta: {'color': 'negra', 'ruedas': 4, 'carga': 1000}
Se han encontrado 0 vehículos con 0 ruedas:
'''


# Ejercicio 3: Triángulo
# -----------------------------------------
# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos, imprimir el
# valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
# isósceles o escaleno).


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor_lado(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

triangulo1 = Triangulo(3, 3, 3) # Crear un triángulo equilátero
triangulo2 = Triangulo(3, 4, 5) # Crear un triángulo escaleno
triangulo3 = Triangulo(5, 5, 7) # Crear un triángulo isósceles

print("Triángulo 1:")
print("Mayor lado:", triangulo1.mayor_lado())
print("Tipo de triángulo:", triangulo1.tipo_triangulo())

print("\nTriángulo 2:")
print("Mayor lado:", triangulo2.mayor_lado())
print("Tipo de triángulo:", triangulo2.tipo_triangulo())

print("\nTriángulo 3:")
print("Mayor lado:", triangulo3.mayor_lado())
print("Tipo de triángulo:", triangulo3.tipo_triangulo())


# La salida será:
'''
Triángulo 1:
Mayor lado: 3
Tipo de triángulo: Equilátero

Triángulo 2:
Mayor lado: 5
Tipo de triángulo: Escaleno

Triángulo 3:
Mayor lado: 7
Tipo de triángulo: Isósceles
'''
'''
En este ejemplo, la clase Triangulo tiene un constructor que inicializa los atributos 
`lado1`, `lado2` y `lado3`. También tiene dos métodos: `mayor_lado` que devuelve el lado 
con mayor longitud, y `tipo_triangulo` que devuelve el tipo de triángulo (equilátero, 
isósceles o escaleno) basado en la longitud de los lados. Luego, se instancian tres objetos
 de Triangulo y se imprimen los valores correspondientes.
'''
'''
Ejercicio 4: Tiempo
Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser
instanciada indicando: los tres atributos, sólo la hora y minuto, o sólo la hora.
Crear además los métodos necesarios para modificar la hora en cualquier
momento de forma manual. Mantenga la integridad de los datos en todo
momento definiendo de tipo “private”. Crear una clase prueba_tiempo que
prueba una hora concreta y la modifique a su gusto mostrándola por pantalla.
'''

class Tiempo:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.__hora, self.__minuto, self.__segundo)

    def cambiar_hora(self, hora, minuto=0, segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

# Clase de prueba
class prueba_tiempo:
    def prueba(self):
        tiempo = Tiempo(10, 30, 45)  # Crear instancia de Tiempo

        print("Hora actual:", tiempo)  # Mostrar hora actual

        tiempo.cambiar_hora(9, 15)  # Cambiar hora y minuto
        print("Hora luego de cambiarla:", tiempo)  # Mostrar hora después del cambio

        tiempo.cambiar_hora(17)  # Cambiar sólo la hora
        print("Hora luego de cambiarla nuevamente:", tiempo)  # Mostrar hora después del cambio


# Ejecutar prueba
prueba = prueba_tiempo()
prueba.prueba()

'''
La salida será:

Hora actual: 10:30:45
Hora luego de cambiarla: 09:15:00
Hora luego de cambiarla nuevamente: 17:15:00


En este ejemplo, la clase Tiempo tiene un constructor que inicializa los atributos `hora`, 
`minuto` y `segundo`. Estos atributos son privados y se acceden a través de sus métodos 
correspondientes. También hay un método especial `__str__` para imprimir la hora en un formato
legible para el usuario.
Además, la clase Tiempo cuenta con un método `cambiar_hora` que permite cambiar la hora actual
en cualquier momento. Se puede cambiar la hora indicando todos los tres valores: hora, minuto
y segundo, o bien, sólo hora y minuto, o sólo hora. 

Luego, hay una clase de prueba `prueba_tiempo` que instancia un objeto de la clase Tiempo 
y llama al método `cambiar_hora` varias veces. Al cambiar la hora, se muestra la hora actual
antes y después del cambio.
'''

'''
Ejercicio 5: Gestión de Donaciones
-------------------------------------
Nos piden que diseñemos un programa para gestionar donaciones de alimentos.
Los productos tienen los siguientes atributos:
Nombre
Cantidad
Tenemos dos tipos de productos:
Perecedero: tiene un atributo llamado días a caducar.
No perecedero: tiene un atributo llamado tipo.
Tendremos una función llamada Calcular, que según cada clase hará una cosa u
otra, a esta función se le envía la cantidad por producto y entidades a las cuáles
se entregarán donaciones.
Debe obtener la cantidad que se enviará a cada entidad, sabiendo que la
distribución debe ser lo más equitativa posible. En caso que sobren
productos, se almacenan para el próximo ciclo de donación.
Además si el producto es perecedero, se informará:
Si le queda menos de 10 días para caducar, la entrega debe hacerse en el
día actual.
Si le queda 1 mes para caducar, la entrega debe hacerse en el plazo de 1
semana.
Si fuera No Perecedero, se informa cuántos productos se entregarán por
entidad y que queda libre la elección de la fecha de entrega siempre que no
supere el mes.
'''
class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def calcular(self, entidades):
        pass

class Perecedero(Producto):
    def __init__(self, nombre, cantidad, dias_caducar):
        super().__init__(nombre, cantidad)
        self.dias_caducar = dias_caducar

    def calcular(self, entidades):
        entrega_inmediata = False
        entrega_semana = False
        for entidad in entidades:
            cantidad_entidad = self.cantidad // len(entidades)
            if self.dias_caducar < 10 and not entrega_inmediata:
                entidad.recibir(self.nombre, cantidad_entidad)
                entrega_inmediata = True
            elif self.dias_caducar < 30 and not entrega_semana:
                entidad.recibir(self.nombre, cantidad_entidad)
                entrega_semana = True
            else:
                entidad.almacenar(self.nombre, cantidad_entidad)

class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo

    def calcular(self, entidades):
        for entidad in entidades:
            cantidad_entidad = self.cantidad // len(entidades)
            entidad.recibir(self.nombre, cantidad_entidad)

class Entidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}

    def recibir(self, nombre_producto, cantidad):
        if nombre_producto in self.inventario:
            self.inventario[nombre_producto] += cantidad
        else:
            self.inventario[nombre_producto] = cantidad

    def almacenar(self, nombre_producto, cantidad):
        self.recibir(nombre_producto, cantidad)

# Ejemplo de uso

producto_perecedero = Perecedero("Leche", 100, 9)
producto_no_perecedero = NoPerecedero("Arroz", 200, "Blanco")

entidad1 = Entidad("Comedor Solidario")
entidad2 = Entidad("Banco de Alimentos")
entidad3 = Entidad("Cáritas")

producto_perecedero.calcular([entidad1, entidad2, entidad3])
producto_no_perecedero.calcular([entidad1, entidad2, entidad3])

print(entidad1.inventario)  # {'Leche': 33, 'Arroz': 66}
print(entidad2.inventario)  # {'Leche': 33, 'Arroz': 66}
print(entidad3.inventario)  # {'Leche': 34, 'Arroz': 68}

'''
En este ejemplo, la clase Producto es la clase base que tiene los atributos nombre y cantidad,
además del método calcular que se especializa en cada clase hija.
La clase Perecedero y NoPerecedero son subclases de Producto y agregan los atributos 
dias_caducar y tipo respectivamente, además de sobrescribir el método calcular para realizar
el cálculo de entrega de productos de acuerdo a sus requisitos.
La clase Entidad representa las organizaciones que reciben las donaciones y tiene un 
inventario de productos recibidos. Tiene los métodos recibir para recibir productos y 
almacenar para almacenar los productos sobrantes.
En el ejemplo de uso, se crean dos productos: uno perecedero y otro no perecedero, 
y tres entidades que recibirán las donaciones. Se llama al método calcular de cada producto
con la lista de entidades como argumento y se imprime el inventario de cada entidad
después del cálculo.
'''
'''
Ejercicio 6: Cuentas Electrónicas
---------------------------------------
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que
es una persona) y cantidad (puede tener decimales). El titular será obligatorio y
la cantidad es opcional.
Implementa los siguientes métodos:
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad
introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
números rojos.
'''
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

'''
En este ejemplo, la clase Persona representa al titular de la cuenta y tiene un solo atributo
nombre.
La clase Cuenta tiene los atributos titular y cantidad, que se ingresan en el constructor. 
El atributo cantidad es opcional y, por defecto, es 0.
La clase Cuenta tiene los métodos mostrar, ingresar y retirar. El método mostrar muestra en la
pantalla el titular y la cantidad de la cuenta. El método ingresar añade una cantidad a la 
cuenta solo si la cantidad es positiva. El método retirar resta una cantidad a la cuenta solo
si la cantidad es positiva.
'''
'''
La clase Cuenta se utilizaría así:
'''
persona1 = Persona("Juan")
cuenta1 = Cuenta(persona1, 1000)

cuenta1.mostrar()  # Titular: Juan, Cantidad: 1000

cuenta1.ingresar(500)
cuenta1.mostrar()  # Titular: Juan, Cantidad: 1500

cuenta1.retirar(3000)
cuenta1.mostrar()  # Titular: Juan, Cantidad: -1500

'''
En este ejemplo, se crea una instancia de la clase Cuenta con un titular llamado "Juan"
y una cantidad inicial de 1000. Luego se llama al método mostrar, para mostrar los datos 
de la cuenta.
Después, se llama al método ingresar con una cantidad de 500 y al método mostrar de nuevo
para comprobar que se añadió correctamente la cantidad. Finalmente, se llama al método 
retirar con una cantidad de 3000, lo que dejará la cuenta en números rojos y se muestra
 el resultado llamando al método mostrar de nuevo.
'''

'''
Ejercicio 7: Bebidas Online
---------------------------------------
Vamos a administrar un ecommerce de bebidas.
En un depósito se guardan las bebidas a comercializar.
Estos productos son bebidas como agua mineral y gaseosas.
De los productos nos interesa saber su identificador (cada uno tiene uno
distinto), cantidad de litros, precio y marca.
Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).
Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene o
no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).
Las operaciones del almacén son las siguientes:
Calcular precio de todas las bebidas: calcula el precio total de todos los
productos del almacén.
Calcular el precio total de una marca de bebida: dada una marca, calcular el
precio total de esas bebidas.
Agregar producto: agrega un producto, si el identificador esta repetido en
alguno de las bebidas, no se agregará esa bebida.
Eliminar un producto: dado un ID, eliminar el producto del depósito.
Mostrar información: mostramos para cada bebida toda su información.
'''

class Bebida:
    def __init__(self, identificador, cantidad_litros, precio, marca):
        self.identificador = identificador
        self.cantidad_litros = cantidad_litros
        self.precio = precio
        self.marca = marca

    def __str__(self):
        return f"ID: {self.identificador}, Marca: {self.marca}, Litros: {self.cantidad_litros}, Precio: {self.precio}"

class AguaMineral(Bebida):
    def __init__(self, identificador, cantidad_litros, precio, marca, origen):
        super().__init__(identificador, cantidad_litros, precio, marca)
        self.origen = origen

    def __str__(self):
        return f"{super().__str__()}, Origen: {self.origen}"

class Gaseosa(Bebida):
    def __init__(self, identificador, cantidad_litros, precio, marca, porcentaje_azucar, promocion=False):
        super().__init__(identificador, cantidad_litros, precio, marca)
        self.porcentaje_azucar = porcentaje_azucar
        self.promocion = promocion
        if self.promocion:
            self.precio *= 0.9  # Aplicar un descuento del 10% si hay promoción

    def __str__(self):
        return f"{super().__str__()}, Azúcar: {self.porcentaje_azucar}, Promoción: {self.promocion}"

class Almacen:
    def __init__(self):
        self.bebidas = []

    def agregar_bebida(self, bebida):
        for b in self.bebidas:
            if b.identificador == bebida.identificador:
                print("Error: ya existe una bebida con ese identificador.")
                return
        self.bebidas.append(bebida)

    def eliminar_bebida(self, identificador):
        for b in self.bebidas:
            if b.identificador == identificador:
                self.bebidas.remove(b)
                return
        print("Error: no existe una bebida con ese identificador.")

    def calcular_precio_todas_bebidas(self):
        total = 0
        for b in self.bebidas:
            total += b.precio
        return total

    def calcular_precio_marca_bebidas(self, marca):
        total = 0
        for b in self.bebidas:
            if b.marca == marca:
                total += b.precio
        return total

    def mostrar_informacion(self):
        for b in self.bebidas:
            print(b)

# Ejemplo de uso
almacen = Almacen()

agua1 = AguaMineral(identificador="A001", cantidad_litros=2.5, precio=20, marca="Manantial", origen="Neuquén")
gaseosa1 = Gaseosa(identificador="G001", cantidad_litros=1.5, precio=35, marca="Coca-Cola", porcentaje_azucar=10, promocion=True)

almacen.agregar_bebida(agua1)
almacen.agregar_bebida(gaseosa1)
almacen.agregar_bebida(Gaseosa(identificador="G002", cantidad_litros=1.5, precio=30, marca="Pepsi", porcentaje_azucar=15, promocion=False))

almacen.mostrar_informacion()

print(f"Precio total de todas las bebidas: {almacen.calcular_precio_todas_bebidas()}")
print(f"Precio total de bebidas de la marca Coca-Cola: {almacen.calcular_precio_marca_bebidas('Coca-Cola')}")

almacen.eliminar_bebida("G002")

almacen.mostrar_informacion()

'''
En este ejemplo, se definen tres clases de bebidas: Bebida, AguaMineral y Gaseosa. 
AguaMineral tiene un atributo adicional origen y Gaseosa tiene atributos adicionales
porcentaje_azucar y promocion.
La clase Almacen tiene un atributo bebidas que es una lista de bebidas. Tiene métodos 
agregar_bebida, eliminar_bebida, calcular_precio_todas_bebidas, calcular_precio_marca_bebidas
y mostrar_informacion. El método agregar_bebida comprueba si el identificador ya existe para
evitar duplicados. El método eliminar_bebida elimina la bebida con el identificador dado
de la lista de bebidas.
El método calcular_precio_todas_bebidas calcula el precio total de todas las bebidas en el
almacen. El método calcular_precio_marca_bebidas calcula el precio total de las bebidas con 
la marca dada. El método mostrar_informacion muestra en la pantalla toda la información de 
todas las bebidas en el almacen.
Por último, se creó una instancia de la clase Almacen, se agregaron algunas bebidas, 
se mostró la información, y se calcularon los precios totales. Luego, se eliminó una bebida
y se mostró la información actualizada.
'''

'''
Ejercicio 8: Mis Libros Favoritos
---------------------------------------------------
Vamos a crear un programa para nuestros libros favoritos.
Queremos mantener una lista de los libros que hemos ido leyendo, calificando
según nos haya gustado más o menos al leerlo.
Para ello, crear la clase Libro, cuyos atributos son el titulo, el autor, el
número de páginas y la calificación que le damos entre 0 y 10.
Crear los métodos para poder modificar y obtener los atributos si tienen
sentido.
Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto
de libros. Se pueden añadir libros que no existan (siempre que haya espacio),
eliminar libros por título o autor, mostrar por pantalla los libros con la mayor
y menor calificación dada y, por último, mostrar un contenido de todo el
conjunto.
'''

class Libro:
    def __init__(self, titulo, autor, num_paginas, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.calificacion = calificacion

    def __str__(self):
        return f"{self.titulo} de {self.autor}. {self.num_paginas} páginas. Calificación: {self.calificacion}"

class ConjuntoLibros:
    def __init__(self, max_libros):
        self.max_libros = max_libros
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < self.max_libros:
            self.libros.append(libro)
            print(f"Libro {libro.titulo} agregado.")
        else:
            print("El conjunto de libros está lleno.")

    def eliminar_libro_por_titulo(self, titulo):
        eliminado = False
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                eliminado = True
                print(f"Libro '{titulo}' eliminado.")
                break
        if not eliminado:
            print(f"No se encontró el libro '{titulo}'.")

    def eliminar_libro_por_autor(self, autor):
        eliminado = False
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                self.libros.remove(libro)
                eliminado = True
                print(f"Libro '{libro.titulo}' eliminado por autor '{autor}'.")
        if not eliminado:
            print(f"No se encontró ningún libro del autor '{autor}'.")

    def mostrar_libros_con_menor_calificacion(self):
        menor_calificacion = min([libro.calificacion for libro in self.libros])
        libros_menor_calificacion = [libro for libro in self.libros if libro.calificacion == menor_calificacion]
        print("Los libros con menor calificación son:")
        for libro in libros_menor_calificacion:
            print(libro)

    def mostrar_libros_con_mayor_calificacion(self):
        mayor_calificacion = max([libro.calificacion for libro in self.libros])
        libros_mayor_calificacion = [libro for libro in self.libros if libro.calificacion == mayor_calificacion]
        print("Los libros con mayor calificación son:")
        for libro in libros_mayor_calificacion:
            print(libro)

    def mostrar_contenido(self):
        print("Contenido de ConjuntoLibros:")
        for libro in self.libros:
            print(libro)

# Ejemplo de uso
conjunto_libros = ConjuntoLibros(max_libros=3)

libro1 = Libro(titulo="El principito", autor="Antoine de Saint-Exupéry", num_paginas=96, calificacion=8)
libro2 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", num_paginas=432, calificacion=10)
libro3 = Libro(titulo="La sombra del viento", autor="Carlos Ruiz Zafón", num_paginas=672, calificacion=9)

conjunto_libros.agregar_libro(libro1)
conjunto_libros.agregar_libro(libro2)
conjunto_libros.agregar_libro(libro3)

conjunto_libros.mostrar_contenido()

conjunto_libros.eliminar_libro_por_titulo("el principito")

conjunto_libros.eliminar_libro_por_autor("Carlos Ruiz Zafón")

conjunto_libros.mostrar_contenido()

conjunto_libros.agregar_libro(Libro(titulo="1984", autor="George Orwell", num_paginas=360, calificacion=7))

conjunto_libros.mostrar_libros_con_menor_calificacion()

conjunto_libros.mostrar_libros_con_mayor_calificacion()

'''
En este ejemplo, se definen dos clases: Libro y ConjuntoLibros. La clase Libro tiene atributos
de título, autor, número de páginas, y calificación. La clase ConjuntoLibros tiene un atributo
max_libros que indica el número máximo de libros que se pueden almacenar en el conjunto y una
lista de libros. Tienen métodos para agregar libros, eliminar libros por título y por autor,
mostrar los libros con la menor y mayor calificación, y mostrar el contenido de todo el 
conjunto.
En este ejemplo se creó una instancia de la clase ConjuntoLibros, se agregaron tres libros,
mostrando la información del conjunto de libros a lo largo del camino. Luego se eliminó el 
libro "El principito" por título y "Carlos Ruiz Zafón" por autor, y se agregó un nuevo libro.
En último lugar se muestran los libros con la menor y mayor calificación.

La salida producida por el código sería similar a la siguiente:

 Libro El principito agregado. Libro Cien años de soledad agregado. Libro La sombra del
 viento agregado. Contenido de ConjuntoLibros: El principito de Antoine de Saint-Exupéry. 
 96 páginas. Calificación: 8 Cien años de soledad de Gabriel García Márquez. 432 páginas. 
 Calificación: 10 La sombra del viento de Carlos Ruiz Zafón. 672 páginas. Calificación: 
 9 Libro 'El principito' eliminado. Libro 'La sombra del viento' eliminado por autor 
 'Carlos Ruiz Zafón'. Contenido de ConjuntoLibros: Cien años de soledad de Gabriel García
 Márquez. 432 páginas. Calificación: 10 Libro 1984 agregado. Los libros con menor 
 calificación son: 1984 de George Orwell. 360 páginas. Calificación: 7 Los libros con mayor 
 calificación son: Cien años de soledad de Gabriel García Márquez. 432 páginas. Calificación:
 10
'''

'''
Ejercicio 9: Cafetera robot
--------------------------------------------------
Cómo diseñaríamos el comportamiento de una cafetera robot?
Desarrolla una clase Cafetera con atributos:
_capacidadMaxima (la cantidad máxima de café que puede contener la
cafetera)
_cantidadActual (la cantidad actual de café que hay en la cafetera).Luego desarrollar los siguientes métodos:
llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la
capacidad.
servirTaza(int): simula la acción de servir una taza con la capacidad indicada.
Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que
quede.
vaciarCafetera(): pone la cantidad de café actual en cero.
agregarCafe(int): añade a la cafetera la cantidad de café indicada.
'''

class Cafetera:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad_actual = 0

    def llenar_cafetera(self):
        self.cantidad_actual = self.capacidad_maxima
        print("Cafetera llena.")

    def servir_taza(self, cantidad):
        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            print(f"Se ha servido una taza de café con {cantidad} ml.")
        else:
            print("No hay suficiente café en la cafetera para llenar la taza.")
            self.cantidad_actual = 0

    def vaciar_cafetera(self):
        self.cantidad_actual = 0
        print("Cafetera vaciada.")

    def agregar_cafe(self, cantidad):
        if self.cantidad_actual + cantidad <= self.capacidad_maxima:
            self.cantidad_actual += cantidad
            print(f"Se han agregado {cantidad} ml de café a la cafetera.")
        else:
            print("La cafetera no tiene suficiente capacidad para agregar esa cantidad de café.")
            self.llenar_cafetera()

# Ejemplo de uso
cafetera = Cafetera(capacidad_maxima=1000)

cafetera.agregar_cafe(800)

cafetera.servir_taza(300)

cafetera.servir_taza(700)

cafetera.llenar_cafetera()

cafetera.agregar_cafe(1100)

cafetera.vaciar_cafetera()

'''
En este ejemplo, se define la clase Cafetera con dos atributos: capacidad_maxima y 
cantidad_actual, que representan la cantidad máxima de café que puede contener la cafetera
y la cantidad actual de café en la cafetera, respectivamente. También se definen cuatro métodos
: llenar_cafetera(), servir_taza(), vaciar_cafetera() y agregar_cafe().
En este ejemplo se crea una instancia de la clase Cafetera, se agrega café a la cafetera,
se sirven dos tazas de café y se muestra el resultado, luego se llena la cafetera y se intenta
agregar más café del que cabe en la cafetera, vaciando la cafetera al final.
'''

'''
Ejercicio 10: Tomamos un Mate
------------------------------------
Modelar una clase Mate que describa el funcionamiento de la conocida bebida
tradicional argentina. La clase debe contener como miembros:
Un atributo para la cantidad de cebadas restantes hasta que se lava el mate
(representada por un número).
Un atributo para el estado (lleno o vacío).
El constructor debe recibir como parámetro n, la cantidad máxima de cebadas
en base a la cantidad de yerba vertida en el recipiente.
Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate
lleno, se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te
quemaste!
Un método beber, que vacía el mate y le resta una cebada disponible. Si se
intenta beber un mate vacío, se debe lanzar una excepción que imprima el
mensaje. El mate está vacío!
Es posible seguir cebando y bebiendo el mate aunque no haya cebadas
disponibles. En ese caso la cantidad de cebadas restantes se mantendrá en 0,
y cada vez que se intente beber se debe imprimir un mensaje de aviso:
Advertencia: "el mate está lavado", pero no se debe lanzar una excepción.
'''

class Mate:
    def __init__(self, n):
        self.cant_cebadas = n
        self.lleno = False

    def cebar(self):
        if self.lleno:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.lleno = True
        print("Mate cebado.")

    def beber(self):
        if not self.lleno:
            raise Exception("El mate está vacío!")
        if self.cant_cebadas > 0:
            self.cant_cebadas -= 1
        else:
            print("Advertencia: el mate está lavado.")
        self.lleno = False
        print("Se ha bebido una cebada.")

'''
En este ejemplo, se define la clase Mate con dos atributos: cant_cebadas y lleno, que 
representan la cantidad de cebadas restantes hasta que se lava el mate y el estado del mate
(lleno o vacío), respectivamente. También se definen dos métodos: cebar() y beber().
El método cebar() llena el mate con agua. Si se intenta cebar con el mate lleno, 
se lanza una excepción que imprime el mensaje ¡Cuidado! ¡Te quemaste!. El método 
beber() vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, 
se lanza una excepción que imprime el mensaje El mate está vacío!. Si la cantidad de cebadas
disponibles es cero, se imprime un mensaje de advertencia: el mate está lavado, pero no se 
lanza una excepción.
'''
'''
Ejemplo de cómo usar esta clase en Python:
'''
# Crear un nuevo Mate con 3 cebadas disponibles
mate = Mate(3)

# Cebamos el mate y lo bebemos 3 veces
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()
mate.cebar()
mate.beber()

# Aquí la cantidad disponible de cebadas es cero
mate.beber()
mate.beber() # Esto no lanza una excepción ya que está lavado

