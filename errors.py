#!/usr/bin/env python3
"""Tratamento de exceções
LBYL - Look Before You Leap

EAFP - Easy to Ask Forgiveness than permission + pythonica
"""
import sys
import os
import logging
import time

log = logging.Logger("errors")

def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries N times."""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()

        except FileNotFoundError as e: # Bare except, w/o error name
            log.error("ERRO: %s", e)
            time.sleep(2)

        else: # executa somente se retorna sucesso
            print("Sucesso!")
        finally: # executa mesmo retornando erro
            print("Execute isso sempre.")
    return []
    

for line in try_to_open_a_file("names.txt", retry=5):
    print(line)

"""
except ZeroDivisionError as e:
    print(f"{str(e)}")
    sys.exit(4)
except AttributeError as e:
    print(f"{str(e)}")
    sys.exit(5)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(2)
"""
