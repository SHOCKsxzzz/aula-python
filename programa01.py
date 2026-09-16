notas = []
while True:
    nota = float(input("Digite a nota: "))
    if nota == 0:
        break
    notas.append(nota)
media = sum(notas) / len(notas)
print(media)
if media >= 7:
    print("aprovado")
else:
    print("reprovado")