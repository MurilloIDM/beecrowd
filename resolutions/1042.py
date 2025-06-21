# LINK: https://judge.beecrowd.com/pt/problems/view/1042

numbers = [int(number) for number in input().split(" ")]

ordered_numbers = sorted(numbers)

[print(number) for number in ordered_numbers]
print()
[print(number) for number in numbers]
