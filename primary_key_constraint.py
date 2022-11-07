
#Una clave principal es una columna o grupo de columnas que se utiliza para identificar la unicidad de las filas de una tabla. Cada tabla tiene una y sólo una clave principal.
#SQLite le permite definir la clave principal de dos maneras:

#Primero, si la clave principal tiene solo una columna, usa la PRIMARY KEYrestricción de columna para definir la clave principal de la siguiente manera:

#CREATE TABLE table_name(
  # column_1 INTEGER NOT NULL PRIMARY KEY,
   #...
#);

## En segundo lugar, en caso de que la clave principal consista en dos o más columnas, utilice la PRIMARY KEYrestricción de la tabla para definir la principal como se muestra en la siguiente declaración.

#CREATE TABLE table_name(
  # column_1 INTEGER NOT NULL,
   #column_2 INTEGER NOT NULL,
   #...
  # PRIMARY KEY(column_1,column_2,...)
#);
