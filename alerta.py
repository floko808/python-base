#!/usr/bin/env python3

"""alarme de temperatura"""
import sys
from typing import Dict

# TODO: Mover para modulo de utilidades.

def is_completely_filled(dict_of_inputs: Dict) -> bool:
    """Returns a boolean telling if a dict is completely filled
    """
    info_size = len(dict_of_inputs)
    filled_size = len([val for val in dict_of_inputs.values() if val is not None])
    return info_size == filled_size
  
def read_inputs_for_dicts(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = int(input(f"{key}: ").strip())
        except ValueError as e:
            print(f"{key} inválida. {str(e)}")
            break


# programa principal

info = {
    "temperatura": None,
    "umidade": None
}

while not is_completely_filled(info):

    read_inputs_for_dicts(info)


temp, humi = info.values()


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