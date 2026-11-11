nome = str(input("Nome do produto: ")).strip().capitalize()
quant = int(input("Quantidade: "))
preco = float(input("Valor do unitário: R$"))

total = quant * preco

print("-=" * 30)
if quant <= 5:
    total_pagar = total - (total * 0.02)
    print(f"Produto: {nome}")
    print(f"TOTAL: {total:.2f}")
    print(f"Desconto de 2%: R${total * 0.02:.2f}")
    print(f"Total a pagar: R${total_pagar:.2f}")
elif quant > 5 and quant <= 10:
    total_pagar = total - (total * 0.03)
    print(f"Produto: {nome}")
    print(f"TOTAL: {total:.2f}")
    print(f"Desconto de 3%: R${total * 0.03:.2f}")
    print(f"Total a pagar: R${total_pagar:.2f}")
elif quant > 10:
    total_pagar = total - (total * 0.05)
    print(f"Produto: {nome}")
    print(f"TOTAL: {total:.2f}")
    print(f"Desconto de 5%: R${total * 0.05:.2f}")
    print(f"Total a pagar: R${total_pagar:.2f}")
