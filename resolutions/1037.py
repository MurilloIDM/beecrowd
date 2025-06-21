# LINK: https://judge.beecrowd.com/pt/problems/view/1037

value = float(input())

if 0 <= value <= 25.00:
    print("Intervalo [0,25]")
elif 25 < value <= 50.00:
    print("Intervalo (25,50]")
elif 50 < value <= 75.00:
    print("Intervalo (50,75]")
elif 75 < value <= 100.00:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
