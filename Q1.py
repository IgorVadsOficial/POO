n1 = float(input("1° bimestre: "))
n2 = float(input("2° bimestre: "))

mp = (n1 * 2 + n2 * 3) / 5

print("-=" * 30)
print(f"Sua nota ponderado foi de: {mp}")

if mp >= 6.0:
    print("Situação: APROVADO!")
elif mp < 2.0:
    print("Situação: REPROVADO!")
else:
    print("Situação: EM PROVA FINAL!")
