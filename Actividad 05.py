while True:
    lista = []
    print("\n --Menu de Analisis de ventas--")
    print("1. Ingrese la lista de ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. venta mas alta y la mas baja")
    print("4. promedio de las ventas")
    print("5. Cuantos dias se superaron Q1000")
    print("6. Clasificaioon de ventas")
    print("7. Salir")
    option=input("Elija una opcioon")
    match option:
        case 1:
            venta = int(input())