# LINK: https://judge.beecrowd.com/pt/problems/view/1024

number_cases = int(input())

for position_case in range(number_cases):
    text = input()
    text_transform = ""

    # Andar 3 posições para direita
    for letter in text:
        if letter.isalpha():
            text_transform += chr(ord(letter) + 3)
            continue

        text_transform += letter

    # Inverter caracteres
    text_transform_list = list(text_transform)
    text_transform_list.reverse()

    text_transform = "".join(text_transform_list)

    # Andar 1 posição para esquerda
    result = ""
    half_value = len(text_transform) // 2
    for position in range(len(text_transform)):
        if (position >= half_value):
            result += chr(ord(text_transform[position]) - 1)
            continue

        result += text_transform[position]

    print(result)
