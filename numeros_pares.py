#!/usr/bin/env python3
"""Núemeros pares até 200"""


pares = []
impares = []
for num in range(1, 201):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Números Pares: {pares}')
print(f'Números Impares: {impares}')