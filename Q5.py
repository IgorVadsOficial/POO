from math import sqrt

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (pow(b, 2)) - ((4 * a) * c)

if delta < 0 or a == 0:
    print("É impossivel realizar a operação! ")

elif delta == 0:
    print("As raízes são reais e iguais! ")
    x = -b / (a * 2)
    print(f"Delta = {delta:.0f}")
    print(f"X = {x:.2f}")

elif delta > 0:
    print("As raízes são reais e diferentes de zero! ")
    x1 = (-b + sqrt(delta)) / (a * 2)
    x2 = (-b - sqrt(delta)) / (a * 2)
    print(f"Delta = {delta:.0f}")
    print(f"X1 = {x1:.2f}")
    print(f"X2 = {x2:.2f}")
