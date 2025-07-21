# Ejercicio Sistema de Parqueadero (Uso de Constructores y Destructores)
# Este ejercicio simula el ingreso y salida de vehículos en un parqueadero usando los principios de POO: __init__ y __del__
# Cada vez que un vehículo entra al parqueadero, se crea una instancia de la clase `Vehiculo`,
# lo cual representa su entrada. Cuando el vehículo sale (el objeto se elimina), se ejecuta automáticamente el destructor para simular la salida del parqueadero.

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        print(f"Vehículo con placa {self.placa} ingresó al parqueadero.")

    def __del__(self):
        print(f"Vehículo con placa {self.placa} salió del parqueadero.")


# Simulación de ingreso y salida
v1 = Vehiculo("ABC-123")
v2 = Vehiculo("XYZ-789")

