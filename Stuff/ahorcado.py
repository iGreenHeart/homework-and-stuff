import random
import os

# Abro el txt y corro un for para guardar las palabras en mayusculas
txtpalabras = open("Stuff/palabras.txt", encoding="utf-8")
archivo = txtpalabras.readlines()
palabras = []
for palabra in archivo:
    palabras.append(palabra.upper())

# Elijo una palabra de mi lista de forma alaeatoria
palabra = list(random.choice(palabras))

# Hago un pop para borrar el salto de linea guardado
palabra.pop()
# Creo los espacios de las letras del intento con un len de mi palabra
palabraintento = list("_"*len(palabra))
intentos = 5  # Inicio intentos en 0, que va a funcionar como mi sistema de vidas
listaletras = []
os.system("cls")
print(f"Bienvenino a mi ahorcado! Tenés {intentos} intentos.")
print("Palabra a adivinar:", " ".join(palabraintento))

while 1:  # Este ciclo se va a repetir hasta que el intento sea igual a la palabra
    # Ingreso el intento + lo conviero a mayusculas para evitar problemas futuros
    letra = input("Poné tu intento: ").upper()

    # Si el usuario ingresa una cadena que es igual a la palabra seleccionada gana el juego.
    if letra == "".join(palabra):
        print("Correcto! La palabra es:", "".join(palabra))
        break

    # Si la letra ingresada ya fue utilizada previamente, vuelve a reiniciar el ciclo.
    if letra in listaletras:
        os.system("cls")  # Limpia la consola
        print("Ya utilizaste esta letra")
    # Actualiza el ahorcado, y vuelve a inicializar
        print("Palabra actualizada:", " ".join(palabraintento))
        print(f"Letras utilizadas {set(listaletras)}")
        print(f"Tenes {intentos} intentos.")
        continue
    # Sumo la letra ingresada a la lista
    listaletras.append(letra)

    # Inicio mi flag en 0 cada ciclo. Si la letra es igual a una de las letras en la lista de la palabra, aumenta flag
    flag = 0
    # Recorro un for con enumerate(), para acceder tanto al indice y a la letra de la palabra
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:  # Si hay un match, entonces la letra va a reemplazar a la letra de mi intento en el indice correspondiente
            palabraintento[indice] = letra
            flag += 1

    # Si mi flag no aumentó en el for anterior, me resta intentos.
    if flag == 0:
        intentos -= 1

    os.system("cls")  # Limpia la consola
    # Actualiza el ahorcado, y vuelve a inicializar
    print("Palabra actualizada:", " ".join(palabraintento))
    print(f"Lista Letras {set(listaletras)}")

    if intentos == 0:  # Si el usuario se quedó sin intentos, termina el programa
        print("Perdiste boludito")
        print("La palabra era:", "".join(palabra))
        break
    elif palabraintento == palabra:  # Si el usuario adivina la palabra, gana
        print("Adivinaste la palabra:", "".join(palabra))
        break
    print(f"Tenes {intentos} intentos.")
