ventas = []
while True:
    print("\n --Menu de Analisis de ventas--")
    print("1. Ingrese la lista de ventas ")
    print("2. Mostrar todas las ventas ingresadas ")
    print("3. venta mas alta y la mas baja ")
    print("4. promedio de las ventas ")
    print("5. Cuantos dias se superaron Q1000 ")
    print("6. Clasificaioon de ventas ")
    print("7. Salir ")
    option=input("Elija una opcion ")
    match option:
        case "1":
            print("Ingreso de ventas")
            day_admitted= int(input("ingrese cuantos dias quiere ingresar "))
            for i in range (day_admitted):
                while True:
                    venta_= input("Ingrese la cantidad de las ventas ")
                    if venta_.isdigit():
                        venta= int(venta_)
                        ventas.append(venta)
                        break
                    else:
                        print("Error datos invalidos, vuelva a intentarlo ")
        case "2":
            print("\n Mostrar todas la ventas realizadas")
            print(ventas)
        case "3":
            print("\n Calculando ventas ")
        case "4":
            print("")
        case "5":
            print("")
        case "6":
            print("hola ")
        case "7":
            print("Estamos slaiendo...")
