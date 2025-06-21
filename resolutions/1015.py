# LINK: https://judge.beecrowd.com/pt/problems/view/1015

import math

valores_plano_um_str = input()
valores_plano_dois_str = input()

valores_plano_um = valores_plano_um_str.split(" ")
valores_plano_dois = valores_plano_dois_str.split(" ")

x1 = float(valores_plano_um[0])
y1 = float(valores_plano_um[1])
x2 = float(valores_plano_dois[0])
y2 = float(valores_plano_dois[1])

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f'{distancia:.4f}')
