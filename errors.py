#!/usr/bin/env python3
"""Tratamento de exceções
LBYL - Look Before You Leap

EAFP - Easy to Ask Forgiveness than permission + pythonica
"""
import sys
import os

try:
    names = open("names.txt").readlines()
    
except FileNotFoundError as e: # Bare except, w/o error name
    print(f"[{str(e)}")
    sys.exit(3)
else: # executa somente se retorna sucesso
    print("Sucesso!")
finally: # executa mesmo retornando erro
    print("Execute isso sempre.")
"""
except ZeroDivisionError as e:
    print(f"{str(e)}")
    sys.exit(4)
except AttributeError as e:
    print(f"{str(e)}")
    sys.exit(5)
"""

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(2)