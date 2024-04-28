import random

victoria = 0
derrota = 0
intentos = 0

def numeroaleatorio():
    return random.randint(1, 3)

def menu ():
    return """
    1. Piedra
    2. Papel
    3. Tijera
    """

def ganaste():
    global victoria, intentos
    victoria += 1
    intentos += 1

def perdiste():
    global derrota, intentos
    derrota += 1
    intentos += 1

def quiengano():
   if victoria == derrota:
       return "empate"
   elif victoria > derrota:
       return "ganaste"
   else:
       return "perdiste"
    


while intentos < 3:
    if victoria == 2 or derrota == 2:
        break
    computadora = numeroaleatorio()
    print ("el numero es: ", computadora)
    print (menu())
    jugador = input("ingrese su eleccion: ")
    if jugador.isdecimal():
        jugador = int(jugador)
        if jugador >=1 and jugador <=3:
            if computadora == jugador:
                print ("empate")
                intentos += 1
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

print (f"el juego ha terminado, {quiengano()}")