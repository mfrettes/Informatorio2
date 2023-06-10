-- DESAFIO N° 7 : GRUPO 18

-- CREACION DE BASE DE DATOS:
create database blog_ong;
use blog_ong;

-- CREACION DE TABLAS Y CORROBORACION CON SELECT:
CREATE TABLE usuario (
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  telefono VARCHAR(20),
  username VARCHAR(50),
  email VARCHAR(50),
  contrasena VARCHAR(100),
  estado BOOLEAN,
  fecha_creacion DATE,
  avatar BLOB,
  es_publico BOOLEAN,
  es_colaborador BOOLEAN,
  es_admin BOOLEAN,
  PRIMARY KEY (id_usuario)
);

SELECT * from usuario;

CREATE TABLE articulo (
  id_articulo INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  titulo VARCHAR(100) NOT NULL,
  resumen TEXT(1000),
  contenido TEXT,
  fecha_publicacion DATE,
  estado BOOLEAN,
  imagen BLOB,
  PRIMARY KEY (id_articulo),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

SELECT * from articulo;

CREATE TABLE comentario (
  id_comentario INT NOT NULL AUTO_INCREMENT,
  id_articulo INT NOT NULL,
  id_usuario INT NOT NULL,
  contenido TEXT,
  fecha_hora DATETIME,
  estado BOOLEAN,
  PRIMARY KEY (id_comentario),
  FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

SELECT * from comentario; 

CREATE TABLE categoria (
  id_categoria INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(100),
  imagen VARCHAR(100),
  estado BOOLEAN,
  PRIMARY KEY (id_categoria)
);

SELECT * from categoria; 

CREATE TABLE categoria_articulo (
  id_articulo INT NOT NULL,
  id_categoria INT NOT NULL,
  PRIMARY KEY (id_articulo, id_categoria),
  FOREIGN KEY (id_articulo) REFERENCES articulo(id_articulo),
  FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

-- PRIMER PUNTO: Comando para introducir admin, colaboradores y usuarios publicos. 
INSERT INTO usuario (nombre, apellido, telefono, username, email, contrasena, estado, fecha_creacion, es_publico, es_colaborador, es_admin) 
VALUES 
	('Hugo','Smahlij','3644222334','HugoS','hugos@gmail.com','fermin123',True,curdate(),False,False,True),
    ('Rocío','Duarte','3644345678','RocioD','rociod@gmail.com','nacho123',True,curdate(),False,True,False),
    ('Maria','Torres','3644990088','MariaT','mariat@gmail.com','maria123',True,curdate(), False,True,False),
    ('Camilo','Diaz','3644558800','CamiloD','camilodz@gmail.com','camilo123',True,curdate(),False,True,False),
    ('Ramiro','Gonzalez','3644507266','RamiroG','ramirog@gmail.com','ramiro123',True,curdate(),False,True,False),
    ('Lucia','Barrios','3644559988','LuciaB','luciab@gmail.com','lucia123',True,curdate(),True,False,False),
	('Camila','Bustos','3644569888','CamilaB','camilab@gmail.com','camila123',True,curdate(),True,False,False),
	('Pedro','Dominguez','3644559768','PedroD','pedrod@gmail.com','pedro123',True,curdate(),True,False,False),
	('Esteban','Pirel','3644554488','EstebalP','estebanp@gmail.com','esteban123',True,curdate(),True,False,False),
	('Sofia','Lopez','3644223348','SofiaL','sofial@gmail.com','sofia123',True,curdate(),True,False,False);

-- SEGUNDO PUNTO: Comando para actualizar rol de colaborador a admin.   
-- Comando:
-- update usuario set es_admin = 'TRUE' where id_usuario = (ID USUARIO A MODIFICAR); 

-- Ejemplo ejecutado:
update usuario set es_admin = true where id_usuario = 2; 

-- TERCER PUNTO: Comando para introducir en la tabla de articulos, 3 art con estado TRUE y 1 con FALSE.
-- Comando:
-- insert into articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado)
-- values
	-- ('ID USUARIO CREADOR', 'Titulo 1', 'Resumen 1', 'Contenido 1', curdate(), True),
    -- ('ID USUARIO CREADOR', 'Titulo 2', 'Resumen 2', 'Contenido 2', curdate(), True),
    -- ('ID USUARIO CREADOR', 'Titulo 3', 'Resumen 3', 'Contenido 3', curdate(), True),
    -- ('ID USUARIO CREADOR', 'Titulo 4', 'Resumen 4', 'Contenido 4', curdate(), False);
    

-- Ejemplo ejecutado:
insert into articulo (id_usuario, titulo, resumen, contenido, fecha_publicacion, estado)
values
	(1, 'Titulo 1', 'Resumen 1', 'Contenido 1', curdate(), True),
	(2, 'Titulo 2', 'Resumen 2', 'Contenido 2', curdate(), True),
    (3, 'Titulo 3', 'Resumen 3', 'Contenido 3', curdate(), True),
    (9, 'Titulo 4', 'Resumen 4', 'Contenido 4', curdate(), False);

-- CUARTO PUNTO: Comando para eliminar el articulo con estado 'False'
-- Comando:
-- delete from articulo where estado = false and id_usuario = (ID DEL USUARIO CON ESTADO FALSE); 

-- Ejemplo ejecutado:
delete from articulo where estado = false and id_usuario = 9; 

-- QUINTO PUNTO: Comando para agregar comentario a articulo.
-- Comando:
-- insert into comentario (id_articulo, id_usuario, contenido, fecha_hora)
-- values
	-- (1, (ID DEL USUARIO QUE COMENTO), 'Comentario 1',  now()),
	-- (1, (ID DEL USUARIO QUE COMENTO), 'Comentario 2',  now()),
    -- (1, (ID DEL USUARIO QUE COMENTO), 'Comentario 3', now()),
    -- (2, (ID DEL USUARIO QUE COMENTO), 'Comentario 4', now()),
    -- (2, (ID DEL USUARIO QUE COMENTO), 'Comentario 5', now());

-- Ejemplo ejecutado:
insert into comentario (id_articulo, id_usuario, contenido, fecha_hora)
values
	(1, 1, 'Comentario 1',  now()),
	(1, 2, 'Comentario 2',  now()),
    (1, 3, 'Comentario 3', now()),
    (2, 3, 'Comentario 4', now()),
    (2, 4, 'Comentario 5', now());

select * from comentario;

-- SEXTO PUNTO: Listar articulos que tengan comentarios, 
-- mostrando titulo, fecha de publicacion, nombre de usuario, fecha y hora que comento. Agrupados por articulos.

SELECT a.titulo, a.fecha_publicacion, u.nombre, c.fecha_hora
FROM articulo a
INNER JOIN comentario c ON a.id_articulo = c.id_articulo
INNER JOIN usuario u ON c.id_usuario = u.id_usuario
ORDER BY a.titulo;


  