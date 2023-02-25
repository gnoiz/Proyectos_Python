#Utilizamos la sentencia Import, donde vamos a importar el módulo random o aleatorio, contiene funciones y elementos que nos 
#permiten trabajar con procesos aleatorios en Python y en este caso necesitamos generar un número aleatorio.
import random


#DEFINIMOS LA FUNCIÓN
def adivina_el_numero(x): #la letra x es un parámetro de la función
    print("El juego consiste en que adivines un número el cual es generado por el programa!")
    
#Para generar el número aleatorio invocamos el nombre del módulo que acabamos de importar (import random) y luego llamamos a la función (randint / random integer)
#random.randint(a, b) == Retorna un entero aleatorio N tal que a <= N <= b. Alias de randrange(a, b+1).
    numero_aleatorio = random.randint(1,x)  #Número aleatorio entre 1 y x (Inclusive).

    prediccion = 0 #Es cero para que no coincida desde el incio con el número aleatorio

#Para realizar la parte repetitiva del proceso utilizaremos el ciclo while, porque es una cantidad indeterminada de veces (hasta que el usuario adivine) 
#La condición señala que el número que se vaya a ingresar no es igual al generado, por ende es True
    while prediccion != numero_aleatorio:
    #Solicitamos al usuario que ingrese un int
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
        if prediccion < numero_aleatorio:
        #Si el número ingresado por el usuario es menor al generado, se envia el siguiente mensaje:
            print("Intenta nuevamente, este número es menor!.")
        elif prediccion > numero_aleatorio:
        #Si el número ingresado por el usuario es mayor al generado, se envia el siguiente mensaje:
            print("Intenta nuevamente, este número es mayor!.")
    #Si el número ingresado es igual al generado, la condición pasa a ser False, por ende el ciclo se detiene inmediatamente, y se envia el siguiente mensaje:
    print(f"Felicitaciones! Adivinaste el número: {numero_aleatorio} correctamente.")


#LLAMAMOS A LA FUNCIÓN
adivina_el_numero(10) #Llamamos a la función y entre parentesís el valor de x, basicamente colocamos el número 10 para que el número aleatorio generado sea entre 1 y 10