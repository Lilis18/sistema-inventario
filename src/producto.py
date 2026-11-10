from typing import Optional

# Error provocado: falta ':'
class Producto
    def __init__(self, codigo: str, nombre: str, precio: float, existencia: int) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self) -> None:
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Existencia en inventario: {self.existencia}")


def buscar_producto(productos: list[Producto], codigo: str) -> Optional[Producto]:
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None


if __name__ == "__main__":
    producto = Producto("P001", "Producto de ejemplo", 19.99, 10)
    encontrado = buscar_producto([producto], "P001")
    if encontrado is not None:
        encontrado.mostrar_informacion()
    else:
        print("Producto no encontrado.")
