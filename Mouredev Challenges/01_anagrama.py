"""
ANAGRAMA
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(elemento1, elemento2):
    lista1 = list(elemento1)
    lista2 = list(elemento2)
    if elemento1 == elemento2:
        return False
    else:
        flag = 0
        for a, b in zip(sorted(lista1), sorted(lista2)):
            print(a, b)
            if a == b:
                continue
            else:
                return False
        return True


es_anagrama = anagrama(input("Primera palabra: ").upper(),
                       input("Segunda palabra: ").upper())
print(es_anagrama)


### La otra forma ###

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("amor", "roma"))
