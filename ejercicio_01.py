print("Bienvenido al programa")
ventas = []
while True:
    print("\n--MENÚ DE OPCIONES--")
    print("1.Ingresar lista de ventas")   #Listo
    print("2.Mostrar todas las ventas ingresadas")   #Listo
    print("3.Calcular la venta mas alta y la mas baja")
    print("4.Calcular promedio de ventas")
    print("5.Contar cuantos días superaron los Q.1000")
    print("6.Clasificacion de cada venta")
    print("7.Salir")
    option=input("\nSeleccione una opcion: ")

    match option:
        case "1":
            days=int(input("Ingrese el numero de días que desea agregar: "))
            if days>0:
                for i in range(days):
                    while True:
                        venta=input("Ingrese la venta del día:")
                        if venta.isdigit():
                            venta_int=int(venta)
                            if venta_int>0:
                                ventas.append(venta)
                                break
                            else:
                                print("Valor invalido, intentelo de nuevo")
                        else:
                            print("Valor invalido, intentelo de nuevo")
            else:
                print("Error al ingresar datos")
        case "2":
            print("\nVentas ingresadas:")
            print(ventas)

        case "3":
            print("Calculando la venta mas alta y la más baja")
            if ventas:
                print("Máximo:", max(ventas))
                print("Mínimo:", min(ventas))
            else:
                print("La lista está vacía")

        case "4":
            promedio=sum(ventas)/len(ventas)
            print(f"El promedio de ventas es{promedio}")

        case "5":
            print("dias superados de los Q.1000")

        case "6":
            print("Clasificacion de cada lista")

        case "7":
            print("Saliendo del programa")
            break
