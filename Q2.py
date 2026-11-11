from math import sqrt

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (pow(b, 2)) - ((4 * a) * c)

print("-=" * 30)
if delta > 0:
    print(f"Valor de Delta = {delta:.0f}")
    x1 = (-b + sqrt(delta)) / (a * 2)
    x2 = (-b - sqrt(delta)) / (a * 2)
    print(f"A equação possui duas raizes reais: X1 = {x1:.0f} e X2 = {x2:.0f}")
elif delta == 0:
    print(f"Valor de Delta = {delta:.0f}")
    x = -b / (a * 2)
    print(f"A equação possui apenas uma raiz real: X = {x:.0f}")
elif delta < 0 or a == 0:
    print(f"Valor de Delta = {delta:.0f}")
    print("A equação não possui raízes reais!")
