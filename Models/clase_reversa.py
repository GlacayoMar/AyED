

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
