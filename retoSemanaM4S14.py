def cargar_contactos():
    """Cargar contactos desde el archivo 'agenda.txt' si existe."""
    contactos = []
    try:
        with open("agenda.txt", "r") as f_agenda:  # Por defecto esta en "r" se dice pero lo añadi.
            for linea in f_agenda:
                partes = linea.strip().split()  # Divide los datos en partes.(.split este metodo es el quie convierte las lineas en una lista)
                nombre = partes[0]
                apellido = partes[1]
                edad = int(partes[3])
                correo = partes[5]
                telefono = partes[7]
                contactos.append([nombre, apellido, edad, correo, telefono])
    except FileNotFoundError:
        print("No se encontró el archivo 'agenda.txt'. Comienza una nueva agenda.")
    return contactos


def guardar_contactos(contactos):
    """Guardar la lista de contactos en el archivo 'agenda.txt'."""
    with open("agenda.txt", "w") as f_agenda:
        for persona in contactos:
            f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Teléfono: {persona[4]}\n')
    print("Datos guardados en agenda.txt")


def mostrar_contactos(contactos):    # se me hizo util y mas facil añadir esta funcion que otras opciones que se me ocurrieron
    """Mostrar contactos numerados."""
    print("\nLista de contactos:")
    for i, persona in enumerate(contactos, start=1):
        print(f"{i}. {persona[0]} {persona[1]} - Edad: {persona[2]}, Correo: {persona[3]}, Teléfono: {persona[4]}")
    print()  # Línea en blanco


def modificar_contacto(contactos):
    """Modificar el contacto seleccionado."""
    mostrar_contactos(contactos)
    
    while True:
        try:
            indice = int(input("Introduce el número del contacto que deseas modificar: ")) - 1
            if indice < 0 or indice >= len(contactos):
                print("Número inválido. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    print(f"Modificando los datos de: {contactos[indice][0]} {contactos[indice][1]}")
    
    # Modificar el nombre, correo y teléfono con opción de dejar los anteriores
    nuevo_nombre = input(f"Introduce el nuevo nombre ({contactos[indice][0]}): ") or contactos[indice][0]
    nuevo_apellido = input(f"Introduce el nuevo apellido ({contactos[indice][1]}): ") or contactos[indice][1]
    nuevo_correo = input(f"Introduce el nuevo correo ({contactos[indice][3]}): ") or contactos[indice][3]
    
    while True:
        try:
            nuevo_telefono = input(f"Introduce el nuevo teléfono ({contactos[indice][4]}): ") or contactos[indice][4]
            int(nuevo_telefono)  # Verificar que sea un número válido
            break
        except ValueError:
            print("Debes introducir un número válido para el teléfono.")

    # Actualizar los datos del contacto
    contactos[indice][0] = nuevo_nombre
    contactos[indice][1] = nuevo_apellido
    contactos[indice][3] = nuevo_correo
    contactos[indice][4] = nuevo_telefono
    
    print(f"Contacto {nuevo_nombre} {nuevo_apellido} modificado correctamente.\n")


def menu():
    """Menú principal del programa."""
    personas = cargar_contactos()

    while True:
        print("1. Agregar persona a la agenda.")
        print("2. Guardar datos en un archivo.")
        print("3. Modificar un contacto.")
        print("4. Mostrar contactos.")
        print("5. Salir.")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            contacto = []
            while True:
                nombre = input("Introduce su nombre: ")
                apellido = input("Introduce su apellido: ")
                if nombre == "":
                    print("No has introducido su nombre.")
                else:
                    contacto.append(nombre)
                    contacto.append(apellido)
                    break

            while True:
                try:
                    edad = int(input("Introduce su edad: "))
                    contacto.append(edad)
                    break
                except ValueError:
                    print("Debes introducir un número.")

            correo = input("Introduce su correo: ")
            contacto.append(correo)

            while True:
                try:
                    telefono = input("Introduce su teléfono: ")
                    int(telefono)
                    contacto.append(telefono)
                    break
                except ValueError:
                    print("Debes introducir un número.")

            personas.append(contacto)

        elif opcion == "2":
            guardar_contactos(personas)

        elif opcion == "3":
            if personas:
                modificar_contacto(personas)
            else:
                print("No hay contactos para modificar. Agrega alguno primero.")

        elif opcion == "4":
            mostrar_contactos(personas)
            input("Presiona Enter para volver al menú...")  # Pausa antes de volver al menú

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Vuelve a intentarlo.")


# Ejecutar el programa
menu()