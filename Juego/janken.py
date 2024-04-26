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
    numero = numeroaleatorio()
    print ("el numero es: ", numero)
    print (menu())
    ingreso = input("ingrese su eleccion: ")
    if ingreso.isdecimal():
        ingreso = int(ingreso)
        if ingreso >=1 and ingreso <=3:
            if numero == ingreso:
                print ("empate")
                intentos += 1
            elif numero == 1 and ingreso == 2:
                print ("papel le gana a piedra")
                victoria += 1
                intentos += 1  
            elif numero == 1 and ingreso == 3:
                print("tijera pierde contra piedra")
                derrota +=1
                intentos += 1
            elif numero == 2 and ingreso == 1:
                print ("papel le gana a piedra")
                derrota += 1 
                intentos += 1 
            elif numero == 2 and ingreso == 3:
                print("tijera le gana al papel")
                victoria +=1
                intentos += 1
            elif numero == 3 and ingreso == 1:
                print ("piedra gana contra tijera")
                victoria += 1
                intentos += 1  
            elif numero == 3 and ingreso == 2:
                print("papel pierde contra tijera")
                derrota +=1
                intentos += 1
        else:
            print ("ingrese un numero valido")
    else:
        print ("ingrese un numero valido")

print (f"el juego ha terminado, {quiengano()}")