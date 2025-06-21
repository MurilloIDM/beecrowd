# LINK: https://judge.beecrowd.com/pt/problems/view/1040

input_notes = input().split()
notes = list(map(lambda note: float(note), input_notes))

average = ((notes[0] * 2) + (notes[1] * 3) +
           (notes[2] * 4) + (notes[3] * 1)) / 10

print(f"Media: {average:.1f}")

if (average >= 5 and average <= 6.9):
    print("Aluno em exame.")

    note_exam = float(input())
    print(f"Nota do exame: {note_exam:.1f}")

    average = (average + note_exam) / 2
    if (average > 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {average:.1f}")
else:
    if (average > 7):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
