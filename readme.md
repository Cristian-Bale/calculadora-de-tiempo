Proyecto de calculadora de tiempo

Su función es calcular el tiempo entre la suma del tiempo de inicio y un período de tiempo; utilice el sistema "am/pm" y puede calcular la cantidad de días transcurridos si se proporciona








Guía de trabajo:


Escriba una función llamada add_time que acepte dos parámetros obligatorios y un parámetro opcional:

una hora de inicio en el formato de reloj de 12 horas (que termina en AM o PM)
un tiempo de duración que indica el número de horas y minutos
(opcional) un día de inicio de la semana, sin distinción entre mayúsculas y minúsculas
La función debe agregar el tiempo de duración a la hora de inicio y devolver el resultado.

Si el resultado se publicará al día siguiente, debería aparecer (next day)después de la hora. Si el resultado se publicará más de un día después, debería aparecer (n days later)después de la hora, donde "n" representa el número de días transcurridos.

Si la función tiene el parámetro opcional "día de inicio de la semana", la salida debe mostrar el día de la semana del resultado. El día de la semana debe aparecer después de la hora y antes del número de días posteriores.

A continuación se muestran algunos ejemplos de los diferentes casos que la función debe gestionar. Preste especial atención al espaciado y la puntuación de los resultados.

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
No importe ninguna biblioteca de Python. Asuma que las horas de inicio son válidas. Los minutos en la duración serán un número entero menor que 60, pero la hora puede ser cualquier número entero.


Espera :1. La llamada add_time('3:30 PM', '2:12')debería devolver '5:42 PM'.
Espera :2. La llamada add_time('11:55 AM', '3:12') debería devolver '3:07 PM'.
Espera :3. Hora prevista de finalización '(next day)'cuando sea el día siguiente.
Espera :4. Se espera que el período cambie de AMa PMen 12:00.
Espera :5. La llamada add_time('2:59 AM', '24:00')debería devolver '2:59 AM (next day)'.
Espera :6. La llamada add_time('11:59 PM', '24:05')debería devolver '12:04 AM (2 days later)'.
Espera :7. La llamada add_time('8:16 PM', '466:02')debería devolver '6:18 AM (20 days later)'.
Espera :8. Se esperaba agregar 0:00para devolver el tiempo inicial.
Espera :9. La llamada add_time('3:30 PM', '2:12', 'Monday')debería devolver '5:42 PM, Monday'.
Espera :10. La llamada add_time('2:59 AM', '24:00', 'saturDay')debería devolver '2:59 AM, Sunday (next day)'.
Espera :11. La llamada add_time('11:59 PM', '24:05', 'Wednesday')debería devolver '12:04 AM, Friday (2 days later)'.
Espera :12. La llamada add_time('8:16 PM', '466:02', 'tuesday') debería devolver '6:18 AM, Monday (20 days later)'.