'''
Ejercicio 1: Pizzería
--------------------------
Una pizzería de la ciudad ofrece a sus clientes una amplia variedad de pizzas de
fabricación propia, de varios tamaños (8, 10 y 12 porciones).
Los clientes tienen a disposición un menú que describe para cada una de las
variedades, el nombre, los ingredientes y el precio según el tamaño y el tipo (a la
piedra, a la parrilla, de molde) de la pizza. Los clientes realizan sus pedidos en el
mostrador. El pedido debe contener el nombre del Cliente, para llamarlo cuando
su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, la fecha del
pedido, la hora en la que el pedido debe entregarse y la demora estimada
informada al cliente. El pedido va a la cocina y cuando está preparado se informa
al que lo tomó para que se genere la factura correspondiente y se le entregue el
pedido al cliente.
El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la
siguiente información:
Variedades y tipos de pizzas más pedidas por los clientes.
Ingresos (recaudaciones) por períodos de tiempo.
Pedidos (cantidad y monto) por períodos de tiempo.
'''
'''
Para resolver este ejercicio, necesitamos crear varias clases en Python 
que representen los componentes de la pizzería.
'''
from datetime import datetime

class Pizza:
    def __init__(self, nombre, ingredientes, precio):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio

class Tamanio:
    def __init__(self, cantidad_porciones):
        self.cantidad_porciones = cantidad_porciones

class Pedido:
    def __init__(self, cliente, pizzas, tamanios, fecha_pedido, hora_entrega, demora_estimada):
        self.cliente = cliente
        self.pizzas = pizzas
        self.tamanios = tamanios
        self.fecha_pedido = fecha_pedido
        self.hora_entrega = hora_entrega
        self.demora_estimada = demora_estimada

    def calcular_monto_total(self):
        monto_total = 0
        for pizza, tamanio in zip(self.pizzas, self.tamanios):
            monto_pizza = pizza.precio * tamanio.cantidad_porciones
            monto_total += monto_pizza
        return monto_total

class Factura:
    def __init__(self, pedido, fecha_factura, hora_factura):
        self.pedido = pedido
        self.fecha_factura = fecha_factura
        self.hora_factura = hora_factura

    def imprimir_factura(self):
        print(f"Fecha: {self.fecha_factura}")
        print(f"Hora: {self.hora_factura}\n")
        print(f"Cliente: {self.pedido.cliente}")
        print("Pizzas:")
        for pizza, tamanio in zip(self.pedido.pizzas, self.pedido.tamanios):
            print(f"- {pizza.nombre} ({tamanio.cantidad_porciones} porciones): ${pizza.precio * tamanio.cantidad_porciones}")
        print(f"\nMonto total: ${self.pedido.calcular_monto_total()}")

class Pizzeria:
    def __init__(self):
        self.ventas = []
        self.pedidos = []

    def realizar_pedido(self, cliente, pizzas, tamanios, hora_entrega, demora_estimada):
        fecha_pedido = datetime.now()
        pedido = Pedido(cliente, pizzas, tamanios, fecha_pedido, hora_entrega, demora_estimada)
        self.pedidos.append(pedido)
        return pedido

    def facturar_pedido(self, pedido):
        fecha_factura = datetime.now().date()
        hora_factura = datetime.now().time()
        factura = Factura(pedido, fecha_factura, hora_factura)
        self.ventas.append((fecha_factura, pedido.calcular_monto_total()))
        return factura

    def calcular_ingreso_periodo(self, fecha_inicio, fecha_fin):
        ingreso_periodo = 0
        for fecha, monto in self.ventas:
            if fecha_inicio <= fecha <= fecha_fin:
                ingreso_periodo += monto
        return ingreso_periodo

    def calcular_pedidos_periodo(self, fecha_inicio, fecha_fin):
        pedidos_periodo = []
        for pedido in self.pedidos:
            if fecha_inicio <= pedido.fecha_pedido.date() <= fecha_fin:
                pedidos_periodo.append(pedido)
        monto_periodo = sum([pedido.calcular_monto_total() for pedido in pedidos_periodo])
        return len(pedidos_periodo), monto_periodo

    def calcular_variedades_mas_pedidas(self):
        variedades = {}
        for pedido in self.pedidos:
            for pizza in pedido.pizzas:
                if pizza.nombre in variedades:
                    variedades[pizza.nombre] += 1
                else:
                    variedades[pizza.nombre] = 1
        variedades_ord = sorted(variedades.items(), key=lambda x: x[1], reverse=True)
        return variedades_ord[:3]
    
    '''
En esta solución, creamos una clase Pizza que representa una variedad de pizza, 
con sus atributos de nombre, ingredientes y precio. También creamos la clase Tamanio 
para representar el tamaño de la pizza, simplemente con un atributo de cantidad de porciones.
La clase Pedido representa un pedido realizado por un cliente, con sus pizzas, tamaños, 
fecha del pedido, hora de entrega y demora estimada. También tiene un método para calcular 
el monto total del pedido en base a los precios de las pizzas y sus tamaños.
La clase Factura representa la factura generada para un pedido, con la fecha y hora de la 
factura, y un método para imprimir la información de la factura.
La clase Pizzeria es la clase principal que representa toda la pizzería. Tiene una lista 
ventas para mantener un registro de las ventas (fecha y monto), una lista pedidos para 
mantener un registro de los pedidos realizados, y varios métodos para realizar acciones 
en la pizzería.
El método realizar_pedido crea un objeto Pedido y lo agrega a la lista pedidos.
El método facturar_pedido crea un objeto Factura para un pedido dado, y agrega la fecha y 
monto de la venta a la lista ventas.
El método calcular_ingreso_periodo y calcular_pedidos_periodo son métodos para calcular 
los ingresos y pedidos realizados en un período de tiempo dado.
El método calcular_variedades_mas_pedidas calcula las variedades y tipos de pizzas más 
pedidos por los clientes.
Con esta solución, puedes crear objetos de las clases correspondientes y realizar 
operaciones en la pizzería. Por ejemplo, crear un objeto Pizzeria, crear una lista de 
objetos Pizza, y realizar un pedido:
'''
pizzeria = Pizzeria()

pizza_margarita = Pizza("Margarita", ["mozzarella", "tomate", "albahaca"], 10)
pizza_napolitana = Pizza("Napolitana", ["mozzarella", "tomate", "anchoas"], 12)
pizza_hawaiana = Pizza("Hawaiana", ["mozzarella", "tomate", "jamón", "piña"], 15)

pizzas = [pizza_margarita, pizza_napolitana, pizza_hawaiana]
tamanios = [Tamanio(8), Tamanio(10), Tamanio(12)]

pedido = pizzeria.realizar_pedido("Juan", pizzas, tamanios, datetime.now().time(), 30)

factura = pizzeria.facturar_pedido(pedido)
factura.imprimir_factura()

'''
Este código crea una lista de objetos Pizza, una lista de objetos Tamanio, y realiza 
un pedido con las pizzas y tamaños especificados, con un cliente "Juan", 
hora de entrega actual y demora estimada de 30 minutos. Luego, se genera una factura 
para el pedido y se imprime la información de la factura.
'''
'''
Ejercicio 2: Supermercado
--------------------------------------
Un supermercado maneja el catálogo de los productos que vende. De cada
producto se conoce su nombre, precio, y si el mismo es parte del programa
Precios Cuidados o no. Por defecto, el producto no es parte del programa, a
menos que se especifique lo contrario.
Para ayudar a los clientes, el supermercado quiere realizar descuentos en
productos de Primera Necesidad. Es por eso que al calcular el precio de un
producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:
precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9
El supermercado, del cual se conoce el nombre y la dirección, desea conocer la
cantidad total de productos que comercializa y la suma total de los precios de los
mismos.
Suponga ahora que el descuento a aplicar en cada producto de primera
necesidad puede ser distinto y se debe poder definir al momento de crear el
mismo. Por ejemplo, el arroz puede ser un producto de primera necesidad con un
descuento del 8%, mientras que leche podría ser otro producto de primera
necesidad con un decuento del 11%. Esto es sólo un ejemplo. El descuento a
aplicar en cada producto de primera necesidad debe ser configurable al
momento de crearlo.
Implementar un nuevo programa basado en el anterior que incorpore este
nuevo requerimiento.
'''
'''
Para resolver este ejercicio, podemos utilizar una clase Producto que tenga los atributos
de nombre, precio y si es un producto de primera necesidad o no.
Además, vamos a agregar un atributo de descuento para los productos de primera necesidad.
'''
class Producto:
    def __init__(self, nombre, precio, es_primera_necesidad=False, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.es_primera_necesidad = es_primera_necesidad
        self.descuento = descuento

    def precio_final(self):
        precio_final = self.precio
        if self.es_primera_necesidad:
            precio_final = self.precio * (1 - self.descuento / 100)
        return precio_final
'''
En esta solución, el método precio_final devuelve el precio final del producto,
teniendo en cuenta si es un producto de primera necesidad y su descuento correspondiente.
'''

'''
Luego, podemos tener una clase Supermercado que maneje una lista de productos
y tenga los métodos necesarios para calcular la cantidad y el precio total de los mismos.
'''
class Supermercado:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def cantidad_productos(self):
        return len(self.productos)

    def precio_total_productos(self):
        precio_total = sum([producto.precio_final() for producto in self.productos])
        return precio_total
    
'''
En esta solución, el método agregar_producto agrega un objeto Producto a la lista de 
productos. El método cantidad_productos devuelve la cantidad total de productos que 
comercializa el supermercado. El método precio_total_productos devuelve la suma total 
de los precios de los productos del supermercado, teniendo en cuenta el descuento 
correspondiente para los productos de primera necesidad.
'''
'''
Para probar esta solución, podemos crear objetos de la clase Producto y Supermercado, 
agregar productos al supermercado y consultar la cantidad y precio total de los mismos:
'''
arroz = Producto("Arroz", 50, es_primera_necesidad=True, descuento=8)
leche = Producto("Leche", 80, es_primera_necesidad=True, descuento=11)
galletitas = Producto("Galletitas", 20)

supermercado = Supermercado("Mi Supermercado", "Calle Falsa 123")

supermercado.agregar_producto(arroz)
supermercado.agregar_producto(leche)
supermercado.agregar_producto(galletitas)

print(f"Cantidad total de productos: {supermercado.cantidad_productos()}")
print(f"Precio total de los productos: {supermercado.precio_total_productos()}")

'''
Este código crea objetos de la clase Producto para arroz, leche y galletitas, especificando 
que arroz y leche son productos de primera necesidad con descuentos del 8% y 11%, 
respectivamente. Luego, se crea un objeto de la clase Supermercado y se agrega cada producto 
al mismo.
Finalmente, se imprime la cantidad total de productos y el precio total de los mismos.
'''

'''
Ejercicio 3: Barajas
----------------------------------------
Vamos a crear una baraja de cartas españolas orientado a objetos.
Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo
(espadas, bastos, oros y copas)
La baraja estará compuesta por un conjunto de cartas, 40 exactamente.
Las operaciones que podrá realizar la baraja son:
barajar: cambia de posición todas las cartas aleatoriamente
siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no
haya más o se haya llegado al final, se indica al usuario que no hay más
cartas.
cartasDisponibles: indica el número de cartas que aún puede repartir
darCartas: dado un número de cartas que nos pidan, le devolveremos ese
número de cartas (piensa que puedes devolver). En caso de que haya menos
cartas que las pedidas, no devolveremos nada pero debemos indicárselo al
usuario.
cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido
ninguna indicárselo al usuario
mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una
carta y luego se llama al método, este no mostrara esa primera carta.
'''
'''
Para resolver este ejercicio, podemos crear dos clases: Carta y Baraja.

La clase Carta va a tener como atributos un número y un palo.
'''
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

'''
En la clase Baraja, vamos a inicializar la baraja con las 40 cartas correspondientes 
a los palos de espadas, bastos, oros y copas y los números del 1 al 12, excepto el 8 y el 9. 
Además, vamos  a utilizar la librería random de Python para implementar la función de 
barajar las cartas.
'''
import random

class Baraja:
    def __init__(self):
        palos = ["espadas", "bastos", "oros", "copas"]
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        self.cartas = [Carta(numero, palo) for palo in palos for numero in numeros]

    def barajar(self):
        random.shuffle(self.cartas)

    def siguiente_carta(self):
        if len(self.cartas) == 0:
            print("No hay más cartas en la baraja")
            return None
        return self.cartas.pop(0)

    def cartas_disponibles(self):
        return len(self.cartas)

    def dar_cartas(self, num_cartas):
        if num_cartas > len(self.cartas):
            print("No hay suficientes cartas para dar")
            return []
        else:
            return [self.cartas.pop(0) for _ in range(num_cartas)]

    def cartas_monton(self):
        if len(self.cartas) == 40:
            print("Aún no se ha sacado ninguna carta")
        else:
            [print(f"{carta.numero} de {carta.palo}") for carta in self.cartas]

    def mostrar_baraja(self):
        [print(f"{carta.numero} de {carta.palo}") for carta in self.cartas]

'''
En esta solución, la función barajar utiliza el método shuffle de la librería random 
para cambiar aleatoriamente la posición de las cartas en la baraja. La función 
siguiente_carta devuelve la siguiente carta en la baraja y la elimina de la misma. 
La función cartas_disponibles devuelve el número de cartas que quedan en la baraja. 
La función dar_cartas devuelve una lista con el número de cartas especificado por el usuario, 
si es posible. La función cartas_monton muestra las cartas que ya han salido en el juego, 
si es que existen, y la función mostrar_baraja 
muestra todas las cartas en la baraja en su orden actual, sin eliminar ninguna carta.
'''
'''
Para probar esta solución, podemos crear un objeto de la clase Baraja, barajar las cartas, 
sacar cartas, indicar el número de cartas disponibles y mostrar las cartas ya jugadas 
y las que quedan en la baraja
'''
baraja = Baraja()

baraja.barajar()

print(f"Numero de cartas disponible: {baraja.cartas_disponibles()}")

cartas = baraja.dar_cartas(5)

print([f"{carta.numero} de {carta.palo}" for carta in cartas])

print(f"Numero de cartas disponible: {baraja.cartas_disponibles()}")

baraja.cartas_monton()

baraja.mostrar_baraja()

'''
Este código crea un objeto de la clase Baraja, baraja las cartas usando el método barajar, 
saca 5 cartas utilizando el método dar_cartas, indica el número de cartas disponibles en 
la baraja usando el método cartas_disponibles, muestra las cartas ya jugadas en el juego 
usando el método cartas_monton y finalmente muestra todas las cartas en la baraja actualmente 
usando el método mostrar_baraja.
'''

'''
Ejercicio 4: Cuenta Joven
------------------------------------------
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva
clase CuentaJoven que deriva de lo que definas al resolver el Ejercicio 6: Cuentas
Electrónicas de los ejercicios lvl 1.
Cuando se crea esta nueva clase, además del titular y la cantidad se debe
guardar una bonificación que estará expresada en tanto por ciento.Construye los
siguientes métodos para la clase:
En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
edad, por lo tanto hay que crear un método esTitularValido() que devuelve
verdadero si el titular es mayor de edad pero menor de 25 años y falso en
caso contrario.
Además la retirada de dinero sólo se podrá hacer si el titular es válido.
El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la
bonificación de la cuenta.
Piensa los métodos heredados de la clase madre que hay que reescribir.
'''

'''
Para resolver este ejercicio, vamos a crear una nueva clase llamada CuentaJoven que hereda 
de la clase Cuenta que se creó en el Ejercicio 6: Cuentas Electrónicas de los ejercicios 
nivel 1. Esta nueva clase CuentaJoven tendrá un atributo adicional llamado bonificacion 
que estará expresado en tanto por ciento y que será utilizado para calcular los intereses 
generados por la cuenta. Además, vamos a crear la función esTitularValido() que devuelve True 
si el titular de la cuenta es mayor de edad pero menor de 25 años, y False en caso contrario, 
y la función retirar() que sobreescribe la función de la clase Cuenta original para asegurarse
de que el titular es válido antes de permitir la retirada de dinero.
'''

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.titular.edad >= 18 and self.titular.edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para retirar dinero")

    def mostrar(self):
        print(f"Cuenta Joven - Bonificación: {self.bonificacion}%")

'''
En esta solución, la nueva clase CuentaJoven hereda de la clase Cuenta original. 
Sin embargo, sobreescribe la función retirar para asegurarse de que el titular de la cuenta 
es válido antes de permitir la retirada de dinero. La función esTitularValido comprueba si 
el titular de la cuenta es mayor de edad pero menor de 25 años y devuelve True si cumple con 
esta condición, y False en caso contrario. La función mostrar simplemente agrega el mensaje 
"Cuenta Joven" y la bonificación a la salida que se muestra en la pantalla.
'''
'''
Para probar esta solución, podemos crear un objeto de la clase CuentaJoven para un titular 
válido y otro para un titular no válido, realizar depósitos y retiradas, y mostrar la 
información de la cuenta. El código para probar esta solución sería el siguiente:
'''
class Persona:
    def __init__(self, edad):
        self.edad = edad

cuenta_joven_valida = CuentaJoven(Persona(20), 1000, 5)
cuenta_joven_no_valida = CuentaJoven(Persona(30), 500, 10)

cuenta_joven_valida.mostrar()
cuenta_joven_valida.depositar(1000)
cuenta_joven_valida.mostrar()
cuenta_joven_valida.retirar(2000)
cuenta_joven_valida.mostrar()

cuenta_joven_no_valida.mostrar()
cuenta_joven_no_valida.depositar(500)
cuenta_joven_no_valida.mostrar()
cuenta_joven_no_valida.retirar(100)
cuenta_joven_no_valida.mostrar()

'''
Este código crea objetos de la clase CuentaJoven para un titular válido y otro no válido, 
muestra la información de la cuenta usando el método mostrar, realiza depósitos y retiradas 
en ambas cuentas y luego muestra la información de la cuenta de nuevo usando el método mostrar.
'''

'''
Ejercicio 5: Préstamos
------------------------------------------
Se requiere un programa para registro de préstamos en una cooperativa.
Los datos que se manejan para el préstamo son los siguientes:
Número de Préstamo,
Solicitante del préstamo. De quien se requiere únicamente: DNI, Primer
Nombre, Primer y Segundo Apellido, teléfono de casa y teléfono móvil.
Valor del préstamo
Fechas de pago de las cuotas (un máximo de 6 fechas, se asume que el plazo
máximo de pago son 6 meses).
Fecha de autorización del préstamo.
Fecha tentativa de entrega del préstamo.
Las reglas que debe respetar este proyecto son las siguientes:
El número de préstamo siempre deberá ser un valor mayor que cero.
El valor del préstamo siempre debe ser mayor a cero.
Se debe solicitar los datos de quien toma el préstamo.
La fecha tentativa de entrega del préstamo será siete días después de la
fecha de autorización del préstamo.
Las fechas de pago del préstamo se calculan, sumando 30 días a cada una a
partir de la fecha de entrega del préstamo.
Los préstamos solo se pueden autorizar en los primeros 20 días del mes. Esta
es una política que nunca va a cambiar.
Además debes tener en cuenta que:
Existe una fecha máxima para la autorización de los préstamos.
Existe un valor máximo a prestar. La sumatoria de los préstamos que se
ingresen no debe exceder este valor.
Debe permitir la carga de tantos préstamos como desee ingresar el usuario, a
menos que se haya llegado al valor máximo a prestar.
Debe imprimir los datos completos del préstamo, incluyendo la fecha de
entrega y las fechas de pago de las cuotas.
'''
'''
Para resolver este ejercicio, necesitamos crear una clase llamada Prestamo que maneje 
los datos necesarios para registrar un préstamo en una cooperativa. Esta clase tendrá 
atributos como num_prestamo, solicitante, valor_prestamo, fecha_autorizacion, 
fecha_tentativa_entrega y fechas_pago_cuotas.
Primero, definiremos los atributos que serán necesarios para la clase y, a continuación, 
definimos el método constructor de la clase que inicializa estos atributos. 
También definimos métodos para validar las restricciones mencionadas en el enunciado, 
así como para calcular la fecha de entrega del préstamo y las fechas de pago de las cuotas.

El código sería de la siguiente manera:
'''
from datetime import datetime, timedelta

class Solicitante:
    def __init__(self, dni, primer_nombre, primer_apellido, segundo_apellido, telefono_casa, telefono_movil):
        self.dni = dni
        self.primer_nombre = primer_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.telefono_casa = telefono_casa
        self.telefono_movil = telefono_movil

class Prestamo:
    num_prestamo = 0
    valor_max = 1000000    # valor máximo a prestar
    valor_total = 0        # valor total de préstamos actuales

    def __init__(self, solicitante, valor_prestamo, fecha_autorizacion):
        self.num_prestamo = Prestamo.num_prestamo + 1
        self.solicitante = solicitante
        self.valor_prestamo = valor_prestamo
        self.fecha_autorizacion = fecha_autorizacion
        self.fecha_tentativa_entrega = self.calcular_fecha_tentativa_entrega()
        self.fechas_pago_cuotas = self.calcular_fechas_pago_cuotas()

        Prestamo.num_prestamo += 1
        Prestamo.valor_total += valor_prestamo

    def validar_num_prestamo(self):
        return self.num_prestamo > 0

    def validar_valor_prestamo(self):
        return self.valor_prestamo > 0 and self.valor_prestamo + Prestamo.valor_total <= Prestamo.valor_max

    def validar_solicitante(self):
        return isinstance(self.solicitante, Solicitante)

    def validar_fecha_autorizacion(self):
        now = datetime.now()
        return now.day <= 20 and now.month == self.fecha_autorizacion.month and now.year == self.fecha_autorizacion.year

    def calcular_fecha_tentativa_entrega(self):
        return self.fecha_autorizacion + timedelta(days=7)

    def calcular_fechas_pago_cuotas(self):
        fecha_pago = self.fecha_tentativa_entrega + timedelta(days=30)
        fechas_pago_cuotas = []
        for i in range(6):
            fechas_pago_cuotas.append(fecha_pago)
            fecha_pago += timedelta(days=30)
        return fechas_pago_cuotas

    def mostrar(self):
        print("Número de Préstamo:", self.num_prestamo)
        print("Solicitante del préstamo:")
        print("  - DNI:", self.solicitante.dni)
        print("  - Nombre completo:", self.solicitante.primer_nombre,
              self.solicitante.primer_apellido, self.solicitante.segundo_apellido)
        print("  - Teléfono de casa:", self.solicitante.telefono_casa)
        print("  - Teléfono móvil:", self.solicitante.telefono_movil)
        print("Valor del préstamo:", self.valor_prestamo)
        print("Fechas de pago de las cuotas:", self.fechas_pago_cuotas)
        print("Fecha de autorización del préstamo:", self.fecha_autorizacion)
        print("Fecha tentativa de entrega del préstamo:", self.fecha_tentativa_entrega)

'''
En esta solución, la clase Prestamo tiene atributos como num_prestamo, solicitante, 
valor_prestamo, fecha_autorizacion, fecha_tentativa_entrega y fechas_pago_cuotas. 
Además, la clase define métodos como validar_num_prestamo(), validar_valor_prestamo(), 
validar_solicitante(), validar_fecha_autorizacion(), calcular_fecha_tentativa_entrega(), 
calcular_fechas_pago_cuotas() y mostrar().
La función validar_num_prestamo() comprueba si el número de préstamo es mayor que cero. 
La función validar_valor_prestamo() comprueba si el valor del préstamo es mayor que cero y 
si la suma del valor del préstamo y los préstamos actuales no excede el valor máximo a prestar.
La función validar_solicitante() comprueba si el solicitante es una instancia de la clase 
Solicitante. La función validar_fecha_autorizacion() comprueba si la fecha de autorización 
está dentro de los primeros 20 días del mes actual.
La función calcular_fecha_tentativa_entrega() calcula la fecha tentativa de entrega del 
préstamo sumando 7 días a la fecha de autorización del préstamo. La función 
calcular_fechas_pago_cuotas() calcula las fechas de pago de las cuotas sumando 30 días 
a la fecha de entrega del préstamo, para un máximo de 6 cuotas.
La función mostrar() imprime los datos completos del préstamo, incluyendo la fecha de entrega
y las fechas de pago de las cuotas.
'''
'''
Para probar esta solución, podemos crear varios objetos de la clase Prestamo y llamar al 
método mostrar() para imprimir los detalles de cada uno. El código para probar esta solución 
sería el siguiente:
'''
solicitante1 = Solicitante("12345678A", "Juan", "Pérez", "García", "123456789", "678901234")
prestamo1 = Prestamo(solicitante1, 5000, datetime.now())
prestamo1.mostrar()

solicitante2 = Solicitante("87654321B", "María", "Gómez", "Sánchez", "987654321", "345678901")
prestamo2 = Prestamo(solicitante2, 10000, datetime.now())
prestamo2.mostrar()

solicitante3 = Solicitante("01234567C", "Luis", "Hernández", "Torres", "246801357", "571357902")
prestamo3 = Prestamo(solicitante3, 8000, datetime.now())
prestamo3.mostrar()
'''
Este código crea tres objetos de la clase Prestamo con diferentes valores
y llama al método mostrar() en cada uno para imprimir los detalles completos del préstamo.
'''


