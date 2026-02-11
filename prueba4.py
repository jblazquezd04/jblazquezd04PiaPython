import random

opcion = (int(random.randint(1, 3)))
opcionUsuario = (int(input("Escoge piedra (1), papel(2) o tijera(3)")))

if(opcionUsuario == 1 or opcionUsuario == 2 or opcionUsuario == 3):
    if(opcionUsuario != opcion):
        if(opcionUsuario == 1 and opcion == 3):
            print("Gana el jugador")
        if(opcionUsuario == 2 and opcion == 1):
            print("Gana el jugador")
        if(opcionUsuario == 3 and opcion == 2):
            print("Gana el jugador")
        if(opcionUsuario == 1 and opcion == 2):
            print("Pierde el jugador")
        if(opcionUsuario == 2 and opcion == 3):
            print("Pierde el jugador")
        if(opcionUsuario == 3 and opcion == 1):
            print("Pierde el jugador")

    if(opcionUsuario == opcion):
        print("Empate")

print(opcionUsuario,",",opcion)