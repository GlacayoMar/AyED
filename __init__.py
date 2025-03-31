from  Models.clase_compra import *
from Models.clase_factura import *
from Models.clase_reversa import *
from Models.clase_superficie import *
from Models.clase_vehiculo import *


def main():
    opciones = {"1": Vehiculo.ejecutar, "2": Factura.ejecutar, "3": Superficie.calcular_area, "4": Compra.ejecutar,
                "5": Reversa.ejecutar}
    while True:
        print(
            "\n===================================\n1. Calcular importe de vehículo\n2. Generar factura"
            "\n3. Calcular área\n4. Calcular compra\n5. Verificar número invertido\n6. Salir"
            "\n===================================")
        opcion = input("Seleccione una opción: ")
        if opcion == "6":
            break
        opciones.get(opcion, lambda: print("Opción no válida."))()


if __name__ == "__main__":
    main()
