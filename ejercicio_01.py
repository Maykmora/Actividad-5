print("Bienvenido al programa")
while True:
    ventas=[]
    print("\n--MENÚ DE OPCIONES--")
    print("1.Ingresar lista de ventas")
    print("2.Mostrar todas las ventas ingresadas")
    print("3.Calcular la venta mas alta y la mas baja")
    print("4.Calcular promedio de ventas")
    print("5.Contar cuantos días superaron los Q.1000")
    print("6. Buscar si una venta específica existe en la lista")
    print("7.Clasificacion de cada venta")
    print("8.Salir")
    option=input("\nSeleccione una opcion: ")

    match option:
        case "1":
            while True:
                venta=input("Ingrese la venta o "0" para salir")
                match venta:
                    case "0":
                        print("Saliendo")
                        break
                    case _:
                        ventas.append(venta)
        case "2":
            print("\nVentas ingresadas:")
            print(ventas)

        case "3":
            print("Calculando la venta mas alta y la más baja")

        case "4":
            promedio=sum(ventas)/len(ventas)
            print(f"El promedio de ventas es{promedio}")

