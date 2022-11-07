#Cada base de datos SQLite contiene una sola "tabla de esquema" que almacena el esquema para esa base de datos. El esquema de una base de datos es una descripción de todas las demás tablas, índices, disparadores y vistas que se encuentran dentro de la base de datos. La tabla de esquema se ve así:

#EJ:

#CREAR TABLA sqlite_schema(
  #teclee el texto,
  #texto de nombre,
  #texto tbl_name,
  #entero de la página raíz,
 # texto sql
#);

#Aquí algunas aclaraciones para poder comprender mejor este ejemplo

#Escribe:
#La columna sqlite_schema.type será una de las siguientes cadenas de texto: 'table', 'index', 'view' o 'trigger' según el tipo de objeto definido. La cadena 'table' se usa tanto para tablas ordinarias como virtuales .

#Nombre:
#La columna sqlite_schema.name contendrá el nombre del objeto. ( Las restricciones UNIQUE y PRIMARY KEY en las tablas hacen que SQLite cree índices internos con nombres de la forma "sqlite_autoindex_TABLE_N", 
# donde TABLE se reemplaza por el nombre de la tabla que contiene la restricción y N es un número entero que comienza con 1 y aumenta en uno con cada restricción vista en la definición de la tabla.

#Nombre_tbl:

#La columna sqlite_schema.tbl_name contiene el nombre de una tabla o vista a la que está asociado el objeto. Para una tabla o vista, la columna tbl_name es una copia de la columna de nombre. Para un índice, tbl_name es el nombre de la tabla que está indexada.

#Página raíz:

#La columna sqlite_schema.rootpage almacena el número de página de la página del árbol b raíz para tablas e índices. Para las filas que definen vistas, activadores y tablas virtuales, la columna de la página raíz es 0 o NULL.

#Texto sql:

#La columna sqlite_schema.sql almacena texto SQL que describe el objeto. Este texto SQL es una instrucción CREATE TABLE , CREATE VIRTUAL TABLE ,
#  CREATE INDEX , CREATE VIEW o CREATE TRIGGER que,
#  si se evalúa con el archivo de base de datos cuando es la base de datos principal de una conexión de base de datos , recrearía el objeto.