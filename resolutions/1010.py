# LINK: https://judge.beecrowd.com/pt/problems/view/1010

object_one = input().split(" ")
object_two = input().split(" ")

object_one_code = int(object_one[0])
object_one_count = int(object_one[1])
object_one_price = float(object_one[2])

object_two_code = int(object_two[0])
object_two_count = int(object_two[1])
object_two_price = float(object_two[2])

value = (object_one_count * object_one_price) + (object_two_count * object_two_price)

print(f'VALOR A PAGAR: R$ {value:.2f}')
