# LINK: https://judge.beecrowd.com/pt/problems/view/1043

data = input().split(" ")
a = float(data[0])
b = float(data[1])
c = float(data[2])

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = (a + b) * (c / 2)
    print(f"Area = {area:.1f}")
