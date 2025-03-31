import math


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


class Factura:
    def __init__(self, nombre_articulo, precio_unitario, cantidad):
        self.nombre_articulo = nombre_articulo
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad

    def calcular_factura(self):
        subtotal = self.precio_unitario * self.cantidad
        descuento = subtotal * 0.12 if subtotal > 1000 else 0
        subtotal_con_desc = subtotal - descuento
        iva = subtotal * 0.15
        total = subtotal_con_desc + iva

        print("\n===== FACTURA =====")
        print(f"Artículo: {self.nombre_articulo}")
        print(f"Precio unitario: ${self.precio_unitario:.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento (12% si aplica): ${descuento:.2f}")
        print(f"Subtotal con descuento: ${subtotal_con_desc:.2f}")
        print(f"IVA (15%): ${iva:.2f}")
        print(f"Total a pagar: ${total:.2f}")
        print("===================\n")

    @staticmethod
    def ejecutar():
        while True:
            nombre_articulo = input("Ingrese el nombre del artículo: ")
            precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
            cantidad = int(input("Ingrese la cantidad requerida: "))

            factura = Factura(nombre_articulo, precio_unitario, cantidad)
            factura.calcular_factura()

            if input("¿Desea calcular otra factura? (s/n): ").strip().lower() != 's':
                break


class Superficie:
    @staticmethod
    def calcular_area():
        opciones = ["Cuadrado", "Círculo", "Rectángulo", "Trapecio", "Triángulo"]
        while True:
            print("\nSeleccione la figura para calcular el área:")
            for i, op in enumerate(opciones, 1):
                print(f"{i}. {op}")

            try:
                opcion = int(input("Ingrese su opción: "))
                if opcion not in range(1, 6):
                    print("Opcion no valida. Intente de nuevo")
                    continue
            except ValueError:
                print("Entrada no válida. Debe ingresar un número entero.")
                continue

            try:
                if opcion == 1:
                    lado = float(input("Ingrese el lado del cuadrado: "))
                    area = lado * lado
                elif opcion == 2:
                    radio = float(input("Ingrese el radio del círculo: "))
                    area = math.pi * radio * radio
                elif opcion == 3:
                    base = float(input("Ingrese la base del rectángulo: "))
                    altura = float(input("Ingrese la altura del rectángulo: "))
                    area = base * altura
                elif opcion == 4:
                    base1 = float(input("Ingrese la base menor del trapecio: "))
                    base2 = float(input("Ingrese la base mayor del trapecio: "))
                    altura = float(input("Ingrese la altura del trapecio: "))
                    area = (base1 + base2) * altura / 2
                elif opcion == 5:
                    base = float(input("Ingrese la base del triángulo: "))
                    altura = float(input("Ingrese la altura del triángulo: "))
                    area = (base * altura) / 2
                else:
                    print("Opción no válida.")
                    continue

                print(f"El área calculada es: {area:.2f}")
            except ValueError:
                print("Entrada no válida. Debe ingresar valores numéricos.")
                continue

            if input("¿Desea calcular otra área? (s/n): ").strip().lower() != 's':
                break


class Compra:
    @staticmethod
    def ejecutar():
        while True:
            docenas = int(input("Ingrese la cantidad de docenas compradas: "))
            precio_por_unidad = 5
            unidades = docenas * 12
            subtotal = unidades * precio_por_unidad
            descuento = subtotal * 0.15 if docenas > 3 else subtotal * 0.10
            obsequios = (docenas - 3) if docenas > 3 else 0
            total_a_pagar = subtotal - descuento

            print("\n======== DETALLE DE COMPRA ========")
            print(f"Cantidad de docenas compradas: {docenas}")
            print(f"Unidades totales: {unidades}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Descuento: ${descuento:.2f}")
            print(f"Total a pagar: ${total_a_pagar:.2f}")
            print(f"Unidades de obsequio: {obsequios}")
            print("====================================\n")

            if input("¿Desea realizar otra compra? (s/n): ").strip().lower() != 's':
                break


class Reversa:
    @staticmethod
    def ejecutar():
        while True:
            numero = int(input("Ingrese un número de tres cifras: "))
            if 100 <= numero <= 999:
                invertido = int(str(numero)[::-1])
                print(f"El número {numero} {'es' if numero == invertido else 'no es'} igual al invertirse.")
            else:
                print("Por favor, ingrese un número de tres cifras.")

            if input("¿Desea verificar otro número? (s/n): ").strip().lower() != 's':
                break


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
