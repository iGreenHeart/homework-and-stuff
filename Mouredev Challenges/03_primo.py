"""
Reto #3: ¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""
for i in range(1, 101):
    if i % 1 == 0 and i % i == 0 and i % 2 == 0:
        print(f"{i} es primo!")
    else:
        print(f"{i} no es primo.")
