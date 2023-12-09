"""
Reto #6: INVIRTIENDO CADENAS
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def reversosistema(cadena):
    invertido = cadena[::-1]
    return invertido


def reverso(cadena):
    longitud = len(cadena)
    cadenareversa = ""
    for i in range(0, longitud):
        cadenareversa += cadena[longitud - i - 1]
    return cadenareversa


print(reverso("hola"))
