#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. Exemplo:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.1"
__author__ = "Fabio Barros"
__license__ = "Unlicense"

from argparse import ArgumentParser
import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("LOGZAO", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, You passed %s, try with --key=value: %s", arg, str(e) 
            )
        sys.exit(1)
    key = key.lstrip("-").strip()
    value = value.strip()
    
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit(1)
    arguments[key] = value



current_language = arguments["lang"]
if current_language is None:
    # TODO repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]


msg = {
    "en_US": "Hello, World!",
    "pt_BR":"Olá, Mundo!",
    "it_IT":"Ciao, Mondo!",
    "es_SP":"Hola, Mundo!",
    "fr_FR":"Bonjour, Monde!",
}

# sets (hash table) - O(1) - constante
# dicts (hash table)

print(
    msg[current_language] * int(arguments["count"])
    )