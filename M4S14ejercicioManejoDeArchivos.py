personas = []


while True: 
    print("1. Agregar persona a la agenda.\n2. Guardar datos en un archivo.")
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
         
        contacto = []
        while True:
            nombre = input("Introduce su nombre: ")
            apellido = input("Introduce su apellido: ")
            if nombre == "":
                print("No has introducido su apellido")
            else:
                contacto.append(nombre)
                contacto.append(apellido)
                break

        while True:
            try:
                edad = int(input("Introduce su edad:  "))
                contacto.append(edad)
                break
            except ValueError:
                print("Debes introducir un número")

        correo = input("Introduce su correo:  ")
        contacto.append(correo)

        while True:
            try:
                telefono = input("Introduce su telefono: ")
                int(telefono)
                contacto.append(telefono)
                break
            except ValueError:
                print ( "Debes introducir un numero" )

        personas.append(contacto)

    elif opcion == "2":
        with open("agenda.txt", "w") as f_agenda:
            for persona in personas:
                f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n')
        print("Datos guardados en agenda.txt")
        break
    else: 
        print("Opcion invalida")
        print("Volver a intentar")