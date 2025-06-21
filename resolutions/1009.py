# LINK: https://judge.beecrowd.com/pt/problems/view/1009

name = input()
salary = float(input())
sales_total = float(input())

value = salary + (sales_total * 0.15)

print(f'TOTAL = R$ {value:.2f}')
