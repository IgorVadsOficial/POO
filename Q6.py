l = int(input("Digite um valor: "))

f1 = 0
f2 = 1
f3 = 0

if l < 0:
    while l < 0:
        l = int(input("Valor invalido! Digite um número positivo: "))

print("~" * 40)
print(f"|{f1}, {f2}, ", end="")

while f3 < l:
    f3 = f1 + f2
    if f3 > l:
        break
    print(f"{f3}, ", end="")
    f1 = f2
    f2 = f3

print("FIM.          |")
print("~" * 40)
