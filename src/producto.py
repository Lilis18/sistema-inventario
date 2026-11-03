class Producto:
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


if __name__ == "__main__":
    producto = Producto("P001", "Producto de ejemplo", 19.99, 10)
    producto.mostrar_informacion()
