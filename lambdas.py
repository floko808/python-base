#!/usr/bin/env python3

def transf_maiusculo(texto):
    return texto.upper()


def transf_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)


names = ["Jujuca", "Billy", "Kyra", "Nina"]

# print(sorted(names, key=len))

print(sorted(names, key=lambda name: len(name)))

print(list(filter(lambda name: name[0].lower() == "k", names)))

print(list(map(lambda name: "Hello " + name, names)))


# Calculadora

operacao = input("Operacao [sum, sub, mul, div]: ").strip()
n1 = input("n1: ").strip()
n2 = input("n2: ").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado da operacao {operacao} de {n1} e {n2} é: {resultado}")

