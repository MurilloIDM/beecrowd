# LINK: https://judge.beecrowd.com/pt/problems/view/1044

data = input().split(" ")

a = int(data[0])
b = int(data[1])

result = a % b == 0 if a > b else b % a == 0

if result:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
