"""
Reto #2: LA SUCESIÓN DE FIBONACCI
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

"""
def fibonacci1():
    contador = 0
    numero = 0
    fibonacci = 0
    anterior = 0
    while contador <= 50:
        print(f"Este es el numero de fibonacci {numero}")
        print(f"Y este es el numero {contador}")
        fibonacci = numero + anterior
        anterior = numero
        numero = fibonacci
        print("- "*10)
        if numero == 0:
            numero += 1
        contador += 1


fibonacci1()

"""

""" Suceción de fibonacci
0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229,
832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169,
63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903,
2971215073, 4807526976, 7778742049, 12586269025
"""


def fibonacci2():
    fibonacci = 0
    n0 = 0
    n1 = 1
    for i in range(0, 50):
        print(f"Este es el numero de fibonacci {n0}")
        fibonacci = n0 + n1
        n0 = n1
        n1 = fibonacci


fibonacci2()
