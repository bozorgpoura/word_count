# Nom: Amir Bozorgpour
# 2023-09-13
# TP1


def count_word(input_string): # Définit une fonction 'count_word' qui prend une 'input_string' comme argument.
    words = len(input_string.split())  # Divisez la chaîne en mots en utilisant l'espace comme séparateur
    return words

input_string = input('Please enter your text:\n')
number_word = count_word(input_string)
print('The number of words in your text is:', number_word) # Affichez le résultat en imprimant le nombre de mots.


