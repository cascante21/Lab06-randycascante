# Randy Cascante Espinoza C11718

## RealTimeDataManager (realtime/datamanager.py)

La clase `RealTimeDataManager` simula la actualización de datos en tiempo real. Utiliza un temporizador para generar datos de temperatura y humedad de manera aleatoria y notifica a los suscriptores a través de un `EventManager` cuando los datos cambian.


# Ejemplo de uso en datamanager.py
real_time_data_manager = RealTimeDataManager()
real_time_data_manager.event_manager.subscribe("actualizacion_datos", imprimir_datos_actualizados)
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

EventManager (events/eventos.py)

La clase EventManager gestiona la suscripción, cancelación de suscripción y notificación de eventos a través de callbacks. Permite a los suscriptores registrarse para recibir notificaciones cuando ocurren eventos específicos.

# Ejemplo de suscripción y notificación en datamanager.py
real_time_data_manager.event_manager.subscribe("actualizacion_datos", imprimir_datos_actualizados)
real_time_data_manager.event_manager.notify("actualizacion_datos", data)

Calculadora (calculator/calculadora.py)

El módulo calculadora.py implementa una calculadora simple que realiza operaciones básicas (+, -, *, /) a través de callbacks y funciones lambda.

# Ejemplo de uso en calculadora.py
user_input = get_user_input()
ejecutar_operacion(user_input, operations['+'])

Operaciones Soportadas
Suma (+)
Resta (-)
Multiplicación (*)
División (/)

Discusión y Ejemplos

Actualización en Tiempo Real
La clase RealTimeDataManager notifica cambios en los datos de temperatura y humedad a través del EventManager. Esto permite que los suscriptores, como en el ejemplo anterior, reciban actualizaciones en tiempo real.

EventManager y Callbacks
La clase EventManager facilita la implementación del patrón de diseño Observer al permitir la suscripción y notificación de eventos. En el ejemplo, se suscribe una función de callback para imprimir datos actualizados cuando se recibe una notificación.

Calculadora con Funciones Lambda
La calculadora utiliza funciones lambda para realizar operaciones específicas. Esto proporciona flexibilidad y extensibilidad al permitir fácilmente agregar nuevas operaciones al diccionario operations.

# Ejemplo de multiplicación con función lambda
result = operations['*'](3, 4)  # Resultado: 12

Este es solo un ejemplo de cómo podrías estructurar tu README. Asegúrate de ajustarlo según las necesidades específicas de tu proyecto y proporcionar ejemplos adicionales o detalles según sea necesario.

