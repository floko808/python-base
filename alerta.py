#!/usr/bin/env python3

"""alarme de temperatura"""
import sys

info = {
    "temperatura": None,
    "umidade": None
}


while True:

    info_size = len(info.values())
    filled_size = len([val for val in info.values() if val is not None])

    if info_size == filled_size:
        break

    keys = info.keys() # extrai as chaves do dict criando uma lista com as chaves

    for key in keys:
        try:
            info[key] = float(input(f"Qual a {key}? ").strip())

        except ValueError as e:
            print(f"{key} inválida. {str(e)}")
            sys.exit(1)

temp = info["temperatura"]
humi = info["umidade"]


if temp > 45.0:
    print("Alerta! Perigo de calor extremo!")
elif temp > 10 and temp <= 30: 
    print("Normal")
elif temp <= 10 and temp > 0:
    print("Frio")
elif temp <= 0:
    print("Frio pra porra!")
elif temp * 3 >= humi:
    print("Perigo! Calor úmido!")