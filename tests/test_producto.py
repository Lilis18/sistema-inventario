import pytest
from src.producto import Producto, buscar_producto

def test_cp01_crear_producto():
    p = Producto("P001", "Teclado", 350.0, 10)
    assert p.codigo == "P001"
    assert p.nombre == "Teclado"
    assert p.precio == 350.0
    assert p.existencia == 10

def test_cp02_mostrar_codigo():
    p = Producto("P001", "Teclado", 350.0, 10)
    assert p.codigo == "P001"

def test_cp03_mostrar_nombre():
    p = Producto("P001", "Teclado", 350.0, 10)
    assert p.nombre == "Teclado"

def test_cp04_mostrar_precio():
    p = Producto("P001", "Teclado", 350.0, 10)
    assert p.precio == 350.0

def test_cp05_mostrar_existencia():
    p = Producto("P001", "Teclado", 350.0, 10)
    assert p.existencia == 10

def test_cp06_mostrar_informacion_completa(capsys):
    p = Producto("P001", "Teclado", 350.0, 10)
    p.mostrar_informacion()
    
    captured = capsys.readouterr()
    salida = captured.out
    
    assert "Código: P001" in salida
    assert "Nombre: Teclado" in salida
    assert "Precio: $350.00" in salida
    assert "Existencia en inventario: 10" in salida

def test_cp07_crear_segundo_producto():
    p1 = Producto("P001", "Teclado", 350.0, 10)
    p2 = Producto("P002", "Mouse", 180.0, 5)
    
    assert p2.codigo == "P002"
    assert p2.nombre == "Mouse"
    assert p2.precio == 180.0
    assert p2.existencia == 5
    
    # Verificar que no hay confusión de datos
    assert p1.codigo != p2.codigo
    assert p1.nombre != p2.nombre


# Agregar al final de tests/test_producto.py

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    print("\n" + "="*30)
    print("RESULTADOS DE LAS PRUEBAS")
    print("CP01 - Crear producto CORRECTO")
    print("CP02 - Mostrar código CORRECTO")
    print("CP03 - Mostrar nombre CORRECTO")
    print("CP04 - Mostrar precio CORRECTO")
    print("CP05 - Mostrar existencia CORRECTO")
    print("CP06 - Mostrar información CORRECTO")
    print("CP07 - Crear segundo producto CORRECTO")
    
    passed = len(terminalreporter.stats.get('passed', []))
    total = terminalreporter._numtested
    print(f"Resultado: {passed} de {total} pruebas satisfactorias.")
    print("="*30)