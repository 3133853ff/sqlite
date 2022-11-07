
#permiten definir expresiones para probar valores cada vez que se insertan o actualizan dentro de una columna.
#Si los valores no cumplen con los criterios definidos por la expresión, SQLite emitirá una violación de restricción y anulará la declaración.
#Las CHECKrestricciones le permiten definir verificaciones de integridad de datos adicionales más allá UNIQUEo NOT NULLpara adaptarse a su aplicación específica.

#La siguiente instrucción muestra cómo definir una CHECKrestricción a nivel de columna:

#CREATE TABLE table_name(
   # ...,
  #  column_name data_type CHECK(expression),
 #   ...
#);


#y la siguiente declaración ilustra cómo definir una CHECKrestricción a nivel de tabla:

#CREATE TABLE table_name(
  #  ...,
 #   CHECK(expression)
#);

#La siguiente declaración crea una nueva tabla llamada contacts:

#CREATE TABLE contacts (
   # contact_id INTEGER PRIMARY KEY,
    #first_name TEXT    NOT NULL,
    #last_name  TEXT    NOT NULL,
   # email      TEXT,
  #  phone      TEXT    NOT NULL
 #                   CHECK (length(phone) >= 10) 
 #);           #en la tabla contacts la columna phone tiene una restriccion CHECK

 
