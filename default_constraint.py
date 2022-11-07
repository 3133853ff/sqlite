
#se usa para definir valores predeterminados para una columna. En general, en la restricción predeterminada de SQLite, se insertará el valor predeterminado en una columna en caso de que el valor de la columna sea nulo o esté vacío.

#A continuación se muestra la sintaxis para agregar una restricción predeterminada en la columna mediante Crear instrucción.

#CREAR TABLA  nombretabla

#(colum1  CLAVE PRIMARIA ENTERA ,

#columna2  TEXTO NO NULO ,

#columna3  ENTERO PREDETERMINADO  valor predeterminado );

##El siguiente es el ejemplo del uso de la restricción predeterminada de SQLite con la instrucción Create para definir la restricción predeterminada en la columna.

#CREATE  LIBRO DE MESA

#(Book_id  INTEGER PRIMARY KEY ,

#nombre_libro  TEXTO NO NULO ,

#Precio  ENTERO POR DEFECTO  100);