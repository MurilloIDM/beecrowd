# LINK: https://judge.beecrowd.com/pt/problems/view/1012

PI = 3.14159

valores_str = input()
valores = valores_str.split(" ")

valor_a = float(valores[0])
valor_b = float(valores[1])
valor_c = float(valores[2])

print(f'TRIANGULO: {((valor_a * valor_c) / 2):.3f}')
print(f'CIRCULO: {(PI * valor_c ** 2):.3f}')
print(f'TRAPEZIO: {(((valor_a + valor_b) * valor_c) / 2):.3f}')
print(f'QUADRADO: {(valor_b ** 2):.3f}')
print(f'RETANGULO: {(valor_a * valor_b):.3f}')
