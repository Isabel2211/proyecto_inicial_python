code:40


import csv
import interfaz
import random


def leer_palabra_secreta():
    with open ("palabras.csv") as csvfile:
        lista = list(csv.DictReader(csvfile))
        diccionario = random.choice(lista)
        palabra_aleatoria = diccionario["palabras"]
        return palabra_aleatoria



def pedir_letra(letras_usadas):
    
    while True:
        print("averigua la primera letra")
        letra = input()
        letra = letra.lower()
        if letra in letras_usadas:
            continue
        if len(letra) > 1:
            print("solo puede ingresar una letra")
            continue
        else:
            letras_usadas.append(letra)
            return letra
    
        

def verificar_letra(letra, palabra_secreta):
        
    if letra in palabra_secreta:
         return True
    
    else: 
        return False

    

def validar_palabra(letras_usadas, palabra_secreta):
    letras_correctas = True
    
    for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_usadas:
                letras_correctas = False
                break 
    return letras_correctas




if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False          

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta()
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')

