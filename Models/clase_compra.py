

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
