a = int(input("Votos do candidato A: "))
b = int(input("Votos do candidato B: "))
c = int(input("Votos do candidato C: "))
nulos = int(input("Votos nulos: "))
brancos = int(input("Votos em branco: "))

total_l = a + b + c + brancos + nulos
v = a + b + c
per_v = (v / total_l) * 100
per_a = (a / total_l) * 100
per_b = (b / total_l) * 100
per_c = (c / total_l) * 100
per_branco = (brancos / total_l) * 100
per_nulos = (nulos / total_l) * 100

print(f"Número total de eleitores: {total_l}.")
print(f"Percentual de votos válidos: {per_v:.2f}%")
print(f"Percentual de votos do candidato A: {per_a:.2f}%")
print(f"Percentual de votos do candidato B: {per_b:.2f}%")
print(f"Percentual de votos do candidato C: {per_c:.2f}%")
print(f"Percentual de votos nulos: {per_nulos:.2f}%")
print(f"Percentual de votos brancos: {per_branco:.2f}%")
