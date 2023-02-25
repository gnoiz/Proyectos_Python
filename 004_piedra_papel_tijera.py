import random


def jugar():    #   Definimos una funcion sin atributos porque no toma ningun valor
    usuario = input("Jugaremos a piedra, papel o tijeras, escribe una opción:\n 'Piedra'\n 'Papel'\n 'Tijeras'\n").lower()   #   Generamos una variable que almacena la respuesta del usuario.
    computadora = random.choice(['piedra','papel','tijeras'])   #   mediante esta variable la computadora va a elegir de forma aleatoria -random.choice- una opcion de la lista indicada -['Piedra','Papel','Tijeras']-
    
    if usuario == computadora:  #   En el caso de que se hayan escogido las mismas opciones retornaremos empate.
        return 'Empate!'
    
    if gano_el_jugador(usuario, computadora):   #   En este caso el jugador ganó la partido, por lo tanto se lo indicamos
        return 'Ganaste!'
    
    return 'Perdiste!'  #   En este caso el jugador perdió la partido, por lo tanto se lo indicamos
    
    
def gano_el_jugador(jugador, oponente):
    #Definimos una funcion con la siguiente logica: piedra>tijeras, asi como tambien tijeras>papel y tambien papel>piedra
    #La funcion retornará el valor True en el caso de que se gane el jugador, con las condiciones mencionadas.
    #Si el jugador pierde (cuando no se aplican las condiciones mencionadas), retornamos un False
    if ((jugador == 'piedra' and oponente == 'tijeras') or (jugador == 'tijeras' and oponente == 'papel') or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False


print(jugar())
        
    