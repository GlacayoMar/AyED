

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
