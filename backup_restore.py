
# RESTORE:

#Hay algunas formas de restaurar una base de datos desde la CLI de SQLite.

#Una forma de hacerlo es simplemente adjuntar una nueva base de datos utilizando el archivo de respaldo (o una copia del mismo). Otra forma de restaurar una base de datos es usar el .restorecomando dot para restaurar el archivo de la base de datos a la base de datos elegida dentro de la CLI de SQLite.

#El .restorecomando fue diseñado específicamente para restaurar una base de datos desde un archivo. Es bastante sencillo de usar.

#Aquí hay un ejemplo:

#ATTACH DATABASE 'pets2.db' AS nombre;
#.restore nombre bak/nombre_backup.db

#Otra forma de restaurar un archivo de respaldo es simplemente adjuntarlo directamente.

#Entonces, en lugar de ejecutar el .restorecomando en el ejemplo anterior, simplemente podría haber hecho lo siguiente:

#ATTACH DATABASE 'bak/nombre_backup.db' AS nombre;
