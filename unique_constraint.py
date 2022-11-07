 
 #Una UNIQUErestricción garantiza que todos los valores de una columna o un grupo de columnas sean distintos entre sí o únicos.
#A continuación se muestra cómo definir una UNIQUErestricción para una columna a nivel de columna:

#CREATE TABLE table_name(
 #   ...,
  #  column_name type UNIQUE,
   # ...
#);

#y para hacer esto en varias columnas se maneja de esta manera:

#CREATE TABLE table_name(
  #  ...,
 #   UNIQUE(column_name1,column_name2,...)
#);