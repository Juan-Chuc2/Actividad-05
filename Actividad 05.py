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
            if ventas:
                for i in range(len(ventas)):
                    print(f"Día {i + 1}: Q{ventas[i]}")
            else:
                print("no hay ventas ingresadas ")
        case "3":
            print("\n Calculando las ventas mas baja y mas alta ")
            if ventas:
                highest_sale = max(ventas)
                lowest_sale = min(ventas)
                print(f" La venta mas alta fue: Q{highest_sale}")
                print(f"La venta mas baja fue: Q{lowest_sale}")
            else:
                print("Verifique, no hay ventas realizadas")
        case "4":
            print("\n Calculando el promedio de ventas")
            addition = 0
            counter = 0
            for n in ventas:
                addition += n
                counter += 1
            if counter >0:
                average= addition/counter
                print(f"la suma es: {addition}")
                print(f"El numero de elementos en lalista es: {counter}")
                print(f"El promedio es: {average}")
            else:
                print("no se puede calcular ningun promedio ya que la lista esta vacia")
        case "5":
            print("\n Calculando cuantos dias se superaon los Q1000 de ventas ")
            if ventas:
                counter1= 0
                for venta in ventas:
                    if venta > 1000:
                        counter1 +=1
                        print(f"Fue(ron) {counter1} día(s) donde las ventas fueron mayores a Q1000")
            else:
                print("No se ha registrado ninguna venta :(")
        case "6":
            print("\n Clasificacion de ventas (Alta, Media, Baja)")
            for venta in ventas:
                if venta >1000:
                    print(f" La venta de {venta}, se clasifica como Venta Alta")
                elif venta >=500 and venta <=1000:
                    print(f"la venta de {venta }, se clasifica como Venta Media")
                else:
                    print(f"la venta de {venta}, esta clasificada como Venta Baja ")
        case "7":
            print("Estamos slaiendo...")
