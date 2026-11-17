# Historial de versiones

## v1.0.2
- Corrección del error detectado en la visualización del precio del producto.
- Validación satisfactoria de todas las pruebas automatizadas con Pytest.
- Generación y publicación del paquete de distribución `sistema-inventario-v1.0.2.zip`.

## v1.0.1 (No liberada - Fallida)
- Se detectó un fallo en las pruebas unitarias (`CP06`) debido a un error en el formato de salida del precio; el pipeline detuvo la liberación automáticamente.

## v1.0.0
- Primera versión del Sistema de Inventario.
- Incorporación de la clase `Producto` y la función `buscar_producto`.
- Implementación de pruebas unitarias con Pytest y automatización CI/CD con GitHub Actions.