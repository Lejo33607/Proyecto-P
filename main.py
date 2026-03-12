Parqueadero = ["."] * 10

while True:
    print("""Bienvenido a mi parqueadero:
1. Ver espacios disponibles.
2. Ingresar vehiculo.
3. Sacar vehiculo.
4. Salir.
""")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        
        print("Parqueadero: ")
        
        for i in range(10):
            if Parqueadero[i] == ".":
                print(f"Espacio {i+1}, está vacio.")
            else:
                
                print(f"Espacio {i+1}, {Parqueadero[i]}.")

    if opcion == "2":

        placa = input("Placa del vehiculo que desea meter: ")
        
        if placa in Parqueadero:
                print("Ya está en el parqueadero.")
        
        elif "." not in Parqueadero:
                print("El parqueadero está lleno.")
        
        else:
            for i in range(10):
                if Parqueadero[i] == ".":
                    Parqueadero[i] = placa
                    print(f"Vehiculo ingresado en {i+1}")
                    break

    if opcion == "3":

        placa = input("Placa del vehiculo que desea sacar: ")

        if placa in Parqueadero:
            posicion = Parqueadero.index(placa)
            Parqueadero[posicion] = ""
            print(f"Vehiculo retirado del espacio {posicion+1}")

        else:
            print("El vehiculo no se encuentra en el parqueadero.")
    
    if opcion == "4":
        print("Saliendo...")
    
        break
