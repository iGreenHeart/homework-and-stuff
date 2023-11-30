import random
import os

palabras = ["ANIMAL", "VETERINARIA", "CANIVALISMO", "MARIPOSA", "CLINICA",
            "OTORRINOLARINGOLOGO", "EDIFICACION", "METROPOLITANO", "ROSQUILLA",
            "ASCENSOR", "CRUCIGRAMA", "MANIPULACION", "ESTRUCTURA"]

palabra=list(random.choice(palabras)) #Elijo una palabra de mi lista de forma alaeatoria
palabraintento=list("_"*len(palabra)) #Creo los espacios de las letras del intento con un len de mi palabra
intentos=5 #Inicio intentos en 0, que va a funcionar como mi sistema de vidas

print(f"Bienvenino a mi ahorcado! Tenés {intentos} intentos.")
print("Palabra a adivinar:", " ".join(palabraintento))

while palabraintento != palabra: #Este ciclo se va a repetir hasta que el intento sea igual a la palabra
    letra=input("Poné tu intento: ").upper() #Ingreso el intento + lo conviero a mayusculas para evitar problemas futuros
    
    for indice, letra_palabra in enumerate(palabra): #Recorro un for con enumerate(), para acceder tanto al indice y a la letra de la palabra
        if letra == letra_palabra: #Si hay un match, entonces la letra va a reemplazar a la letra de mi intento en el indice correspondiente
            palabraintento[indice] = letra 
            intentos +=1 #En caso de haber un match, los intentos se mantienen igual
    
    os.system("cls") #Limpia la consola
    print("Palabra actualizada:", " ".join(palabraintento)) #Actualiza el ahorcado, y vuelve a inicializar
    
    intentos-=1 #Si no hubo match previamente, se resta 1 intento. Si hubo, queda igual
    
    if intentos == 0: #Si el usuario se quedó sin intentos, termina el programa
        print("Perdiste boludito")
        print("La palabra era:", "".join(palabra))
        break
    elif palabraintento == palabra: #Si el usuario adivina la palabra, gana
        print("Adivinaste la palabra:", "".join(palabra))
        break
    print(f"Tenes {intentos} intentos.")