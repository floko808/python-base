#!/usr/bin/env python3
"""Exibe relaatório decrianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""

__version__ = "0.0.3"

# TO DO 

sala1 = ["Fabio", "Billy", "Nina", "Kyra", "Ana Julia"]
sala2 = ["Karim", "Tina", "Penelope"]

aula_ingles = ["Fabio", "Billy","Tina","Nina"]
aula_bons_modos = ["Karim", "Ana Julia", "Penelope", "Kyra"]

# lista alunos em cada ativade por sala

atividades = [
    ("Inglês", aula_ingles), 
    ("Bons modos", aula_bons_modos),
    ]

print("-" * 40)

for nome_ativ, atividade in atividades:
    print(f"Alunos da atividade {nome_ativ}\n")
    aula_s1 = set(sala1) & set(atividade)
    aula_s2 = set(sala2).intersection(atividade)
   
#    for aluno in atividade:
#        if aluno in sala1:
#            aula_s1.append(aluno)
#        elif aluno in sala2:
#            aula_s2.append(aluno)

    print(f"Sala 1 {aula_s1}")
    print(f"Sala 2 {aula_s2}")
    print("-" * 40)

