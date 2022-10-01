#!/usr/bin/env python3

# definicao ou atribuicao

# atribuicao
def nome_da_funcao():
    return None


# assinatura -> *args, **kargs
def nome_da_funcao1(*args, **kargs):
    return None

def nome_da_funcao2():
    """Funcao XPTO faz batatinha
    DOC
    """
    return None

# type hints
def funcao1(a: int, b: int, c: int) -> int:
    resultado = a + b + c
    return resultado

def func1(a, b, c):
   return a*2, b*2, c*2

v1, v2, v3 = func1(2,3,4)

# passagem de argumentos com desempacotamento
# normal
def soma(n1, n2):
    """Faz a some de dois números
    """
    return n1 + n2

# argumentos em sequencia
args = (10, 20) # tuple

# print(soma(args[0], args[1]))

# posicional
print(soma(*args))

# argumentos com dicionários nomeados
kargs = {"n2": 90, "n1": 100}
print(soma(**kargs))


lista_de_valores_para_somar = [
    {"n2": 90, "n1": 110},
    {"n2": 90, "n1": 120},
    {"n2": 90, "n1": 130},
    {"n2": 90, "n1": 140},
    (200,300),
    [123,456],
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item)) # recebendo dicionários nomeados
    else:
        print(soma(*item)) # recebendo argumentos em seq

