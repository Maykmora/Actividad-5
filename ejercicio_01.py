print("Bienvenido al programa")
ventas = []
while True:
    print("\n--MENÚ DE OPCIONES--")
    print("1.Ingresar lista de ventas")   #Listo
    print("2.Mostrar todas las ventas ingresadas")   #Listo
    print("3.Calcular la venta mas alta y la mas baja") #listo
    print("4.Calcular promedio de ventas")
    print("5.Contar cuantos días superaron los Q.1000")
    print("6.Clasificacion de cada venta")
    print("7.Salir")
    option=input("\nSeleccione una opcion: ")

    match option:
        case "1":
            print("\n--INGRESAR VENTA--")
            days=int(input("Ingrese el numero de días que desea agregar: "))
            if days>0:
                for i in range(days):
                    while True:
                        venta=input(f"Ingrese la venta del día {i+1}:")
                        if venta.isdigit():
                            venta_int=int(venta)
                            if venta_int>0:
                                ventas.append(venta_int)
                                break
                            else:
                                print("Valor invalido, intentelo de nuevo")
                        else:
                            print("Valor invalido, intentelo de nuevo")
            else:
                print("Error al ingresar datos")
        case "2":
            print("\n--HISTORIAL DE VENTAS--")
            for i in range(len(ventas)):
                print(f"Día {i}: {ventas[i]}")

        case "3":
            print("\n--VENTAS--")
            if ventas:
                mayor=max(ventas)
                menor=min(ventas)
                dia_mayor=ventas.index(mayor)
                dia_menor=ventas.index(menor)
                print(f"La venta mas alta fue Q.{mayor} en el día {dia_mayor}")
                print(f"La venta mas baja fue Q.{menor} en el día {dia_menor}")
            else:
                print("La lista está vacía")

        case "4":
            if ventas:
                print("\n--PROMEDIO--")
                promedio=sum(ventas)/len(ventas)
                print(f"El promedio de ventas es {promedio:.1f}")
            else:
                print("No hay ventas registradas para calcular el promedio")

        case "5":
            print("\n--CONTADOR--")
            if ventas:
                contador=0
                for venta in ventas:
                    if venta>1000:
                        contador+=1
                print(f"La cantidad de días que se superaron los Q.1000 fueron: {contador}")
            else:
                print("No hay ventas registradas para calcular la cantidad de dias que pasan los Q.1000")

        case "6":
            print("\n--CLASIFICACION DE LISTAS--")
            if ventas:
                venta_baja = []
                venta_media = []
                venta_alta = []
                for venta in ventas:
                    if ventas[venta]<500:
                        venta_baja.append(ventas[venta])
                    elif 500<=venta<1000:
                        venta_media.append(ventas[venta])
                    else:
                        venta_alta.append(ventas[venta])
            else:
                print("No hay ventas registradas para poder clasificarlas")

        case "7":
            print("Saliendo del programa")
            break

        case _:
            print("Opcion invalida, intentelo de nuevo")
