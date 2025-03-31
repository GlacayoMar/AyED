import math


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

