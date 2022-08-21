#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.0.1"
__author__ = "Fabio"


# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

base = range(1, 11)


def tabuada(base,num):
    print(f"Tabuada do {num}")
    for x in base:
        print(f"{num} * {x} = {num*x}")
    print("------------------")

def tabuada_1_a_10():
    for tab in base:
        tabuada(base, tab)

tabuada_1_a_10()