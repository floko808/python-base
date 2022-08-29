#!/usr/bin/env python3
"""Cadastro de Produto"""

__version__ = "0.0.1"


import pprint

# snake case  something_separated_with_underscore_and_not_capitalize
produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Fabio",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
    
}

#pprint.pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(f'O cliente {compra["cliente"]["nome"]} comprou o produto {compra["produto"]["nome"]} e a \
quantidade de {compra["quantidade"]} unidade(s) \
dando um total de R$ {total_compra}')
