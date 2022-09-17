#!/usr/bin/env python3


import sys
import logging

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

ocupados = {} # acumulador

try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": int(dias)
        }

except FileNotFoundError as e:
    logging.error("Arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)



quartos = {} # acumulador


try:
    for line in open(QUARTOS_FILE):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco), # TODO : Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }

except FileNotFoundError as e:
    logging.error("Arquivo %s não existe", QUARTOS_FILE)
    sys.exit(1)



print("Reversa Hotel Pythonico")
print('-' * 63)
if len(ocupados) == len(quartos):
    print("Hotel Lotado!")
    sys.exit(1)

nome_cliente = input("Nome do cliente: ").strip()
head = ['Número', 'Nome do Quarto','Preço', 'Disponibilidade']

print('-' * 63)
print('Lista de quartos')
print('-' * 63)
print(f'{head[0]:6} - {head[1]:14} - {head[2]:17} - {head[3]}')
for codigo, quarto in quartos.items():
    nome = quarto['nome']
    preco = quarto['preco']
    disponivel = False if not quarto['disponivel'] else True
    # TODO: substituir por vírgula
    print(f"{codigo:<6} - {nome:<14} - Preço: R$ {preco:<7.2f} - Disponível: {disponivel}")


try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(0)
except KeyError:
    print(f"O quarto número {num_quarto} não existe.")
    sys.exit(0)
except ValueError:
    logging.error("Número inválido!")
    sys.exit(0)

try:
    dias = int(input("Quantos dias: ").strip())
except ValueError:
    logging.error("Número inválido!")
    sys.exit(0)


nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
total = preco_quarto * dias


print(f"{nome_cliente} você escolheu o quarto {nome_quarto} por {dias} dias e vai custar R${total:.2f}.")

if input("Confirma? [Y/n]").strip().lower() in ("y", "yes"):
    with open(RESERVAS_FILE, "a") as file_:
        file_.write(f"{nome_cliente},{num_quarto},{dias}\n")
else:
    print("Operação cancelada.")
