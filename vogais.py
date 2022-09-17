#!/usr/bin/env python3

words = []

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word: # condição de parada
        break
    final_word = ""
    for char in word:
        # TODO: Removar acentuação usando função
        if char in 'aeiouAEIOU':
            final_word +=  char * 2
        else:
            final_word += char

    words.append(final_word)

print(*words, sep="\n")