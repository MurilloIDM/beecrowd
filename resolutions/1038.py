# LINK: https://judge.beecrowd.com/pt/problems/view/1038

values = input().split(" ")

product_code = values[0]
product_amount = int(values[1])

price_total = 0

match product_code:
    case "1":
        price_total = product_amount * 4.00
    case "2":
        price_total = product_amount * 4.50
    case "3":
        price_total = product_amount * 5.00
    case "4":
        price_total = product_amount * 2.00
    case "5":
        price_total = product_amount * 1.50

print(f"Total: R$ {price_total:.2f}")
