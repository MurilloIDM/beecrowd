# LINK: https://judge.beecrowd.com/pt/problems/view/1013

PI = 3.14159

valores_str = input()
valores = valores_str.split(" ")

valor_a = int(valores[0])
valor_b = int(valores[1])
valor_c = int(valores[2])

maior_a_b = (valor_a + valor_b + abs(valor_a - valor_b)) / 2
maior = (valor_c + maior_a_b + abs(valor_c - maior_a_b)) / 2

print(f'{int(maior)} eh o maior')
