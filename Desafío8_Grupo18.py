'''
Desafío 8: Principios de programación orientada a objetos
-----------------------------------------------------------
Requisitos técnicos:
- Herencia
- Encapsulamiento
Crear las siguientes clases con sus atributos y métodos.
Clase Usuario
 atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de
registro, avatar, estado, online
 métodos: login(), registrar()
Clase Publico(Usuario)
 atributo: es_publico
 métodos: registrar(), comentar()
clase Colaborador(Usuario)
 atributos: es_colaborador
 métodos: registrar(), comentar(), publicar()
clase Articulo
 id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
clase Comentario
 id, id_articulo, id_usuario, contenido, fecha_hora, estado
Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y
logueado, código que permita comentar al Publico y además publicar al Colaborador.
'''
import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenna):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__username = username
        self.__email = email
        self.__contrasenna = contrasenna
        self.__fecha_registro = datetime.datetime.now()
        self.__avatar = None
        self.__estado = "Activo"
        self.__online = False

    def login(self, username, contrasenna):
        if username == self.__username and contrasenna == self.__contrasenna:
            self.__online = True
            return True
        else:
            return False

    def registrar(self):
        # Código para registrar al usuario en la base de datos
        pass

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenna):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenna)
        self.__es_publico = True

    def comentar(self, contenido):
        # Código para enviar comentario
        pass

class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasenna):
        super().__init__(id, nombre, apellido, telefono, username, email, contrasenna)
        self.__es_colaborador = True

    def publicar(self, titulo, resumen, contenido):
        # Código para publicar artículo
        pass

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__titulo = titulo
        self.__resumen = resumen
        self.__contenido = contenido
        self.__fecha_publicacion = datetime.datetime.now()
        self.__imagen = None
        self.__estado = "Publicado"

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.__id = id
        self.__id_articulo = id_articulo
        self.__id_usuario = id_usuario
        self.__contenido = contenido
        self.__fecha_hora = datetime.datetime.now()
        self.__estado = "Publicado"

# Registro y login de usuario
usuario = Publico(1, "Juan", "Pérez", "1234567890", "juanp", "juanp@mail.com", "contrasenna")
usuario.registrar()
usuario.login("juanp", "contrasenna")

# Publicar artículo como colaborador
colaborador = Colaborador(2, "Ana", "García", "0987654321", "anag", "anag@mail.com", "contrasenna")
colaborador.login("anag", "contrasenna")
colaborador.publicar("Título del artículo", "Resumen del artículo", "Contenido del artículo")

# Comentar como usuario público
usuario.comentar("Este es un comentario en el artículo publicado")

'''
En este ejemplo, la clase Usuario tiene los atributos id, nombre, apellido, teléfono, username, email,
 contrasenna, fecha de registro, avatar, estado y online, además de los métodos login() y registrar().

Las clases Publico y Colaborador son subclases de la clase Usuario y agregan el atributo es_publico
 y es_colaborador respectivamente, además de los métodos comentar() y publicar().

La clase Articulo tiene los atributos id, id_usuario, titulo, resumen, contenido, fecha_publicacion,
 imagen y estado.
 
La clase Comentario tiene los atributos id, id_articulo, id_usuario, contenido, fecha_hora y estado.

En el código de ejemplo, se crea un usuario público y se registra y se conecta. Luego se crea un colaborador
que se conecta y publica un artículo. Finalmente, el usuario público deja un comentario en el artículo publicado.
'''

