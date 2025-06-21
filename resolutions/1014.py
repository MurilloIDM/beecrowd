# LINK: https://judge.beecrowd.com/pt/problems/view/1014

valor_x = int(input())  # Distância total percorrida
valor_y = float(input())  # Total de combustível gasto

consumo_medio = valor_x / valor_y
print(f'{consumo_medio:.3f} km/l')
