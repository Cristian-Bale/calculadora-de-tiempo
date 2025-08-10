import streamlit as st
from main import add_time 

# Título y descripción de la app
st.title('Calculadora de Tiempo 🕰️')
st.markdown('Introduce una hora de inicio, una duración y, opcionalmente, un día de la semana para calcular la hora final. ¿Para qué sirve? para sumar tiempo a hora determinada')

# Campos de entrada para el usuario
start_time = st.text_input('Hora de inicio (ej. "3:00 PM")', '3:00 PM')
duration = st.text_input('Duración (ej. "3:10")', '3:10')
day_of_week = st.text_input('Día de la semana (opcional)', '')

# Botón para ejecutar la función
if st.button('Calcular hora'):
    try:
        # Llamar a tu función con los datos del usuario
        if day_of_week:
            result = add_time(start_time, duration, day_of_week)
        else:
            result = add_time(start_time, duration)
        
        # Mostrar el resultado
        st.success(f'El resultado es: {result}')
    except Exception as e:
        # Manejo de errores si la entrada es incorrecta
        st.error(f'Ocurrió un error. Asegúrate de que el formato de las horas sea correcto.')
        st.write(e)