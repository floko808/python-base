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
import logging

# LOGGING BOILERPLATE
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("LOGZAO", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = sys.argv[1:]

#valid_operations = ("sum", "sub", "mul", "div")

# Function dicts
operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

path = '.' #os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

while True:
    # Validação
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

    if operation not in operations:
        print("Operação inválida!")
        print(operations)
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

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(2)

    result = operations[operation](n1, n2)

    print(f"O resultado é {result}")

    try:
        with open(filepath, "a") as log:
            log.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        log.error("%s", str(e))
        sys.exit(2)

    arguments = None

    if input("Pressione enter para continuar ou qualquer tecla para sair."):
        break


