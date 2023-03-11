import random       #8    Importamos el modulo random para invocar la palabra de la lista de palabras
import string       #     Este modulo nos permite trabajar con str, lo utilizo en el la variable     abecedario = set(string)


from ahorcado_palabras import palabras #5  utilizamos un import para justamente importar un solo elemento de este archivo.
                                            #   importa un elemento de un modulo que creamos
from ahorcado_diagramas import vidas_diccionario_visual       #importamos este modulo para trabajar con vidas_diccionario_visual en el print de la linea 52

def obtener_palabra_valida(palabras): #6  Definimos la función, obtener palabras validas con un parametro de la lista de palabras
                                    #7   Seleccionamos luego una palabra al azar de la lista de palabras validas con el modulo random

    palabra = random.choice(palabras)   #9    una vez importado el modulo random invocamos la función choice, que nos permite escoger una opcioón al azar de una secuencia
    #10     creamos un ciclo while para filtar simbolos, asi de esa manera solamente se ingresan palabras.
    while '-' in palabra or ' ' in palabra:

        palabra = random.choice(palabras)

    return palabra.upper()  #11     de esta manera invocamos la palabra de la lista, pero con UPPER para que quede más lindo

        
def ahorcado():     #1   Definimos una función sin parametros por ende parentesís vacios
    print("Jugaremos al ahorcado!")     #2   Lo primero que va a ver el jugador cuando inicie el juego
    
    #3  Creamos una variable "palabra" que almacene una palabra de una lista de palabras a traves de una 
    #función que vamos a definir "obtener palabra valida", elemento palabras es una lista de palabras que podremos seleccionar para el juego.
    #4  Al ser una lista larga de palabras, la creamos en otro archivo: 005_ahorcado_palabras.py
    palabra = obtener_palabra_valida(palabras)  
    
    #11     Una vez obtenida la palabra necesitamos realizar revisiones a 3 conjuntos, las letras ya adivinadas, las que faltan adivinar y el abecedario
    #       La revisión la realizamos mediante 3 variables
    #       Para adivinar la palabra tenemos que adivinar cada una de sus letras, asi que creamos un conjunto -set() 
    #       los conjuntos nos permiten guardar elementos sin elementos repetidos
    letras_por_adivinar = set(palabra) 
    #       creamos otros conjunto, en este caso vacío porque van a estar las letras que el jugador logre adivinar
    letras_adivinadas = set()
    #       Importamos el modulo: [import string] para poder trabajar con strings, contiene todas las letras mayusculas 
    #       en el catalogo de caracteres ascii, lo cual retorna una lista de todo el abecedario en mayuscula [sin la Ñ, por lo tanto la lista de palabras tampoco tiene Ñ]
    abecedario = set(string.ascii_uppercase)
    #       Definimos otra variable, la cantidad de vidas, o chances que tiene el jugador de adivinar la palabra.
    vidas = 7   
    #       Esta variable se va a ir actualizando con el estado del modulo [ahorcado_diagramas]
    #       Se crea un ciclo while, en este caso mientras existan letras pendientes y mientras el jugador tenga vidas ( > 0)
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {''.join(letras_adivinadas)}!") # el metodo join une todos los elementos de un conjunto o una secuencia con el caracter especificado entre comillas " ".
        
    #       Mostrando el estado actual de la palabra por adivinar creando una lista.
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
    #       Para cada letra en la palabra, en la palabra original que se seleccionó para el juego decimos, incluye esa letra si la letra ha sido adivinada, si la letra está en el conjunto de letras adivinadas, 
    #       si no está en el conjunto de letras adivinadas pero si está en la palabra significa que todavia no se ha adivinado, y en ese caso agregamos un "-".
    #       List Comprehension, es una forma de escribir las listas en una sola linea, especificando lo que queremos incluir en esa lista dada alguna condición.
    #   Mostrando el estado del ahorcado:
        print(vidas_diccionario_visual[vidas])
    #   Mostrando las letras separadas por un espacio:
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_jugador = input("Escoge una letra: ").upper() #pedimos al jugador una letra y la convertimos en mayúscula
        
    #   Procesamos la letra ingresada por el jugador:
    #   Si la letra ingresada por el jugador esta dentro del conjunto del abecedario y no en las letras que están dentro 
    #   del conjunto de letras_adivinadas, se añade la letra al conjunto de letras ingresadas:
        if letra_jugador in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_jugador)
            
    #   Si la letra que ingresó el usuario está en el conjunto de letras que falta por adivinar, entonces vamos a quitar 
    #   esa letra del conjunto de letras que falta por adivinar.
    #   Si la letra está en la palabra, quitar la letra del conjunto de letras pendientes por adivinar, si no está en la palabra quitar una vida.
            if letra_jugador in letras_por_adivinar:
                letras_por_adivinar.remove(letra_jugador)
                print("")
            else:
                vidas = vidas - 1
                print(f"\n Tu letra: {letra_jugador}, no está en la palabra.")
#       Si la letra escogida por el usuario ya fue ingresada:
        elif letra_jugador in letras_adivinadas:
            print("\n Ya elegiste esa letra, escoge otra.")
#       Si el jugador ingresa cualquier cosa:
        else:
            print("\n Esta letra no es válida...")
        
#   El juego llega a esta linea cuando se adivinaron todas las letras de la palabra o cuando se agotan las vidas del jugador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f" Ahorcado, perdiste...\n La palabra era {palabra}.")
#   Si el jugador tiene vidas y se acabó el bucle, el jugador ganó
    else:
        print(f"Muy bien!, la palabra era {palabra}. \n Ganaste!")
        
        
#Ejecutamos el juego llamando a la función del juego...
ahorcado()