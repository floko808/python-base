#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.0.2"
__author__ = "Fabio"


base = range(1, 11)


def tabuada(base,num):
    print("{:-^18}".format(f"Tabuada do {num}"))
    for n1 in base:
        resultado = num * n1
        print("{:^18}".format(f"{num} x {n1} = {resultado}"))
    print("#"*18)

def tabuada_1_a_10():
    for tab in base:
        tabuada(base, tab)

tabuada_1_a_10()