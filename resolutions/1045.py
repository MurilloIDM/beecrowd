# LINK: https://judge.beecrowd.com/pt/problems/view/1045

data = input().split(" ")

numbers = [float(number) for number in data]
numbers.sort(reverse=True)

a = numbers[0]
b = numbers[1]
c = numbers[2]

if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")

    if a ** 2 > (b ** 2) + (c ** 2):
        print("TRIANGULO OBTUSANGULO")

    if a ** 2 < (b ** 2) + (c ** 2):
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c and a == c:
        print("TRIANGULO EQUILATERO")

    if (a == b and b != c) or (b == c and a != b):
        print("TRIANGULO ISOSCELES")
