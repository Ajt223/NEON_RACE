import random

def jugar():
    carril = 1
    puntaje = 0
    tiempo = 0
    escudo = 0
    velocidad = 0
    jugando = True

    print("\n===== MODO LOCAL =====")

    while jugando:
        print("\nTiempo:", tiempo)
        print("Puntaje:", puntaje)
        print("Carril:", carril)
        movimiento = input("A = izquierda / D = derecha: ").upper()

        # Movimiento
        if movimiento == "A" and carril > 1:
            carril = carril - 1
        elif movimiento == "D" and carril < 2:
            carril = carril + 1

        # Eventos aleatorios
        evento = random.randint(1, 5)
        if evento == 1:
            obstaculo = random.randint(1, 2)
            print("Obstaculo en carril:", obstaculo)
            if obstaculo == carril:
                if escudo > 0:
                    print("Escudo activado")
                else:
                    print("GAME OVER")
                    jugando = False
        elif evento == 2:
            item = random.randint(1, 3)
            if item == 1:
                velocidad = 10
                puntaje = puntaje + 800
                print("Aumento de velocidad")
            elif item == 2:
                escudo = 8
                puntaje = puntaje + 500
                print("Escudo activado")
            elif item == 3:
                print("Pista despejada")

        # Duración de habilidades
        if velocidad > 0:
            velocidad = velocidad - 1
        if escudo > 0:
            escudo = escudo - 1
        tiempo = tiempo + 1
        if tiempo % 60 == 0:
            puntaje = puntaje + 1000

    print("\nPuntaje final:", puntaje)
    print("Regresando al menú...")
