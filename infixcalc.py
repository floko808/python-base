#!/usr/bin/env python3

"""Calculadora Infix.

Funcionamento:

[operação] [n1] [n2]

Operações
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ inflixcalc.py sum 5 2
7

$ inflixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = "0.1.0"

import sys
import os
from datetime import datetime

arguments = sys.argv[1:]

# TODO: exceptions
if not arguments:
    operation = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]

elif len(arguments) != 3:
    print("Número de argumentos inválidos.")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação inválida!")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
n1, n2 = validated_nums


# TODO: Function dicts
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")


print(f"O resultado é {result}")
