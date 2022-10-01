#!/usr/bin/env python3

nome = "Global"
numero = 1
flag = True

def funcao():
    # escopo local
    nome = "Local"

    def funcao_interna(): # inner function or closure
        # escopo local da funcao_internas
        nome = "Interna"
        print(nome)
        return nome

    print("Escopo local da funcao:", locals())
    funcao_interna()
    print(nome)

    return nome

funcao()
print(nome)