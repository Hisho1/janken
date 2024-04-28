import random

victoria = 0
derrota = 0
intentos = 0
puntos = 0
jugador =""
jugadores ={}

def numeroaleatorio():
    return random.randint(1, 3)

def menu ():
    return """
    1. Piedra
    2. Papel
    3. Tijera
    """

def ganaste():
    global victoria, intentos, puntos
    victoria += 1
    intentos += 1
    puntos += 1

def perdiste():
    global derrota, intentos, puntos
    derrota += 1
    intentos += 1
    puntos -= 1

def empate():
    global intentos
    intentos += 1

def quiengano():
   if victoria == derrota:
       return "empate"
   elif victoria > derrota:
       return "ganaste"
   else:
       return "perdiste"
    
def juego ():
    computadora = numeroaleatorio()
    print (menu())
    jugador = input("ingrese su eleccion: ")
    if jugador.isdecimal():
        jugador = int(jugador)
        if jugador >=1 and jugador <=3:
            if computadora == jugador:
                print ("empate")
                empate()
            elif jugador == 1 and computadora == 2:
                print ("Piedra pierde contra papel")
                perdiste()  
            elif jugador == 1 and computadora == 3:
                print("Piedra gana a tijera")
                ganaste()
            elif jugador == 2 and computadora == 1:
                print ("papel gana a piedra")
                ganaste()
            elif jugador == 2 and computadora == 3:
                print("papel pierde contra tijera")
                perdiste()
            elif jugador == 3 and computadora == 1:
                print ("Tijera pierde contra piedra")
                perdiste()
            elif jugador == 3 and computadora == 2:
                print("Tijera gana contra papel")
                ganaste()
        else:
            print ("ingrese un numero valido")
    else:
        print ("ingrese un numero valido")

jugador = input("ingrese su nombre: ")
while True:
    juego()
    if victoria == 2 or derrota == 2 or intentos == 3:
        print (f"El juego ha terminado, {quiengano()}")
        jugar_otra_vez=input("Jugar de nuevo s/n: ")
        if jugar_otra_vez.lower() == "s":
            victoria = 0
            derrota = 0
            intentos = 0
        else:
            print (f"{jugador}, tu puntuacion fue: {puntos}")
            print ("Se termino el juego")
            break

    