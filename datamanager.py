import time
import random
import threading
from eventos import EventManager  # Asegúrate de importar la clase EventManager desde el archivo eventos.py

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
        # Notificar a través del EventManager cuando los datos cambian
        self.event_manager.notify("actualizacion_datos", self.data)

if __name__ == "__main__":
    def imprimir_datos_actualizados(data):
        print("Datos en tiempo real actualizados:", data)

    real_time_data_manager = RealTimeDataManager()

    # Suscribir el callback a EventManager
    real_time_data_manager.event_manager.subscribe("actualizacion_datos", imprimir_datos_actualizados)

    # Iniciar actualizaciones en tiempo real en segundo plano
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
