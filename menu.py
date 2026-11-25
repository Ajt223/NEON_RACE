while True:
    requisitos = input("¿Su computadora cumple con los requisitos mínimos? (1. Sí / 2. No): ")
    if requisitos == "1":
        print("\n¡Requisitos cumplidos!")
        break
    elif requisitos == "2":
        print("No cumples con los requisitos mínimos. Saliendo...")
        exit()
    else:
        print("Opción inválida. Seleccione 1 o 2.")

while True:
    print("\n===== NEON RACE =====")
    print("1. Local")
    print("2. Multijugador")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        import local
        local.jugar()
    elif opcion == "2":
        import multijugador
        multijugador.jugar()
    elif opcion == "3":
        print("Gracias por su visita a Neon Race. ¡Hasta pronto!")
        break
    else:
        print("Seleccione una opción válida.")
