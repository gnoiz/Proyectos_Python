#La base del juego es la misma que el juego "Adivina el número", solamente que esta vez la computadora va a intentar adivinar el número.
import random  #importamos la función random


def adivina_el_numero_computadora(x):   #Definimos la función, la x es un parametro, es el parametro superior en este caso

    print("El juego consiste en que la computadora adivine un número generado por el usuario!") #Print de presentación del juego
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.") #Solicitamos al usuario que ingrese un número entre 1 y un intervalo especifico
    # x es la limite superior de un intervalo
    #Vamos a definir los intervalos entre 1 y x mediante variables
    limite_inferior = 1 #[1,x]
    limite_superior = x
    
    #Generamos otra variable con el valor de la respuesta del usuario.
    respuesta = "" #Se le pregunta al usuario si es el número que seleccionó, es una cadena vacia porque va a almacenar la respuesta del usuario
    while respuesta != "c": #usamos un ciclo while porque no sabemos cuantas veces tenemos que iterar
        #generamos la predicción
        if limite_inferior != limite_superior: #los limites no son iguales
            prediccion = random.randint(limite_inferior, limite_superior) #en la funcion establecemos los intervalos
            #función random.randint() correspondiente a número aleatorio entero
        else:
            prediccion = limite_inferior #si los limites son iguales, tambien podria ser limite_superior
        
        #Obtener una respuesta del usuario
        respuesta = input(f"Mi predicción es {prediccion}.\n Si es muy alta, ingresa (A).\n Si es muy baja, ingresa (B).\n Si es correcta ingresa (C).\n").lower()
        
        if respuesta == "a": #si la predicción es muy alta reducimos el intervalo
            limite_superior = prediccion - 1
        #intervalo inicial: [1,10]
        #Predicción: 6,     #   es un ejemplo, la prediccion se encuentra dentro de 1 y 10
        #Respuesta: "a",    #   en este caso el usuario nos indica que el limite es muy alto, por ende sabremos que el número es menor que la predicción
        #Intervalo: [1,5]   #   actualizamos el intervalo cambiando el limite superior (limite_superior = prediccion - 1)
        elif respuesta == "b":
            #intervalo inicial: [1,10]
            #predicción: 6  #  ejemplo de predicción
            #respuesta: "b",    #   en este caso el usuario nos indica que el limite es muy bajo, por ende sabremos que el número es mayor que la predicción
            #intervalo: [7,10]  #   ahora pasaremos a buscar en el intervalo entre 7 y 10
            limite_inferior = prediccion + 1
    
    print(f"La computadora adivinó tu número correctamente: {prediccion}.")
    
    
adivina_el_numero_computadora(10)