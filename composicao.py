#!/usr/bin/env python3

""""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Fabio"
    "João", 
    "Breno", 
    "Brian", 
    "Bruno",
]

"""
for name in names:
    if name.lower().startswith("b"):
        print(name)
"""

# estilo funcional
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print("-" * 30)
# estilo procedural
print("Estilo procedural")
def starts_with_b(text):
    return text[0].lower() == "b"

filtro =  filter(starts_with_b, names)
filtro = list(filtro)
print(*filtro, sep="\n")