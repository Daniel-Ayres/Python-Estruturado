def entrada_dados():
    coeficiente = float(input("Digite o valor do coeficiente: "))
    return coeficiente

def calc_delta(a, b, c):
    delta = b * b - 4 * a * c
    return delta

import numpy as np

def calcular_raizes(a, b, c, delta):
    if delta < 0:
        resultado = 'A equação não possui raízes nos números reais'
    elif delta == 0:
        x = -b / (2 * a)
        resultado = f'A equação possui apenas uma raiz: {x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'A equação possui raízes: {x1}, {x2}'

    return resultado
