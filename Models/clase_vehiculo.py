

class Vehiculo:
    def __init__(self, tipo, kilometros=0, toneladas=0):
        self.tipo = tipo.lower()
        self.kilometros = kilometros
        self.toneladas = toneladas

    def calcular_importe(self):
        if self.tipo == "bicicleta":
            return 100
        elif self.tipo in ["moto", "carro"]:
            return self.kilometros * 30
        elif self.tipo == "camion":
            return (self.kilometros * 30) + (self.toneladas * 25)
        else:
            print("Tipo de vehículo no válido.")
            return 0

    @staticmethod
    def ejecutar():
        while True:
            tipo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camión): ").strip().lower()
            if tipo == "bicicleta":
                vehiculo = Vehiculo(tipo)
            else:
                kilometros = float(input("Ingrese la cantidad de kilómetros recorridos: "))
                toneladas = float(input("Ingrese la cantidad de toneladas transportadas: ")) if tipo == "camion" else 0
                vehiculo = Vehiculo(tipo, kilometros, toneladas)

            importe = vehiculo.calcular_importe()
            print(f"El importe a pagar es {importe} cordobas")

            if input("¿Desea calcular otro importe? (s/n): ").strip().lower() != 's':
                break

