import random

def jugar():
    carril_j1 = 1
    carril_j2 = 4
    puntaje_j1 = 0
    puntaje_j2 = 0
    escudo_j1 = 0
    escudo_j2 = 0
    tiempo = 0

    print("\n===== MODO MULTIJUGADOR =====")

    while tiempo < 120:
        print("\nTiempo:", tiempo)
        print("Jugador 1:", puntaje_j1, "Carril:", carril_j1)
        print("Jugador 2:", puntaje_j2, "Carril:", carril_j2)

        # Movimiento jugador 1
        movimiento_j1 = input("Jugador 1 (A / D): ").upper()
        if movimiento_j1 == "A" and carril_j1 > 1:
            carril_j1 = carril_j1 - 1
        elif movimiento_j1 == "D" and carril_j1 < 4:
            carril_j1 = carril_j1 + 1

        # Movimiento jugador 2
        movimiento_j2 = input("Jugador 2 (J / L): ").upper()
        if movimiento_j2 == "J" and carril_j2 > 1:
            carril_j2 = carril_j2 - 1
        elif movimiento_j2 == "L" and carril_j2 < 4:
            carril_j2 = carril_j2 + 1

        # Eventos aleatorios
        evento = random.randint(1, 5)
        if evento == 1:
            obstaculo = random.randint(1, 4)
            print("Obstaculo en carril:", obstaculo)
            if carril_j1 == obstaculo:
                if escudo_j1 > 0:
                    print("Jugador 1 protegido")
                else:
                    puntaje_j1 = puntaje_j1 - 600
            if carril_j2 == obstaculo:
                if escudo_j2 > 0:
                    print("Jugador 2 protegido")
                else:
                    puntaje_j2 = puntaje_j2 - 600
        elif evento == 2:
            item = random.randint(1, 3)
            carril_item = random.randint(1, 4)
            print("Item en carril:", carril_item)
            if carril_j1 == carril_item:
                if item == 1:
                    puntaje_j1 = puntaje_j1 + 800
                elif item == 2:
                    escudo_j1 = 8
                    puntaje_j1 = puntaje_j1 + 500
                elif item == 3:
                    print("Jugador 1 limpia la pista")
            if carril_j2 == carril_item:
                if item == 1:
                    puntaje_j2 = puntaje_j2 + 800
                elif item == 2:
                    escudo_j2 = 8
                    puntaje_j2 = puntaje_j2 + 500
                elif item == 3:
                    print("Jugador 2 limpia la pista")

        # Reducir duración del escudo
        if escudo_j1 > 0:
            escudo_j1 = escudo_j1 - 1
        if escudo_j2 > 0:
            escudo_j2 = escudo_j2 - 1
        tiempo = tiempo + 1

    # Resultado final
    print("\n===== FIN DE LA CARRERA =====")
    print("Puntaje jugador 1:", puntaje_j1)
    print("Puntaje jugador 2:", puntaje_j2)
    if puntaje_j1 > puntaje_j2:
        print("¡Gana el Jugador 1!")
    elif puntaje_j2 > puntaje_j1:
        print("¡Gana el Jugador 2!")
    else:
        print("¡Empate!")
    print("Regresando al menú...")
