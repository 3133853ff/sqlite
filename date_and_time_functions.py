
#SQLite admite seis funciones de fecha y hora de la siguiente manera:

#fecha ( valor de tiempo, modificador, modificador, ... )
#tiempo ( valor de tiempo, modificador, modificador, ... )
#fecha y hora ( valor-hora, modificador, modificador, ... )
#julianday( tiempo-valor, modificador, modificador, ... )
#unixepoch( valor-tiempo, modificador, modificador, ... )
#strftime( formato, valor de tiempo, modificador, modificador, ... )

#Las seis funciones de fecha y hora toman un valor de hora opcional como argumento, seguido de cero o más modificadores. La función strftime() también toma una cadena de formato como primer argumento.

#Los valores de fecha y hora se pueden almacenar como

#texto en un subconjunto del formato ISO-8601 ,
#números que representan el día juliano , o
#Números que representan el número de segundos desde (o antes) 1970-01-01 00:00:00 UTC (la marca de tiempo de Unix).

#Todas las funciones de fecha y hora acceden a valores de tiempo en cualquiera de los formatos de tiempo anteriores.

#La función date() devuelve la fecha como texto en este formato: AAAA-MM-DD.

#La función time() devuelve la hora como texto en este formato: HH:MM:SS.

#La función datetime() devuelve la fecha y la hora como texto en sus mismos formatos: AAAA-MM-DD HH:MM:SS.

#Examples

#Compute the current date.


#1:
#SELECT date();
#Compute the last day of the current month.

#2:
#SELECT date('now','start of month','+1 month','-1 day');
#Compute the date and time given a unix timestamp 1092941466.

#3:
#SELECT datetime(1092941466, 'unixepoch');
#SELECT datetime(1092941466, 'auto'); -- Does not work for early 1970!