def ehprimo(n):

    cont = 0
    divisiveis = list()

    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1
            divisiveis.append(i)
    if cont == 2:
        return "V"
    else:
        return "F"


def ehpar(n):
    if n % 2 == 0:
        return "V"
    else:
        return "F"


def ehamigo(n1, n2):

    divisiveln1 = list()
    divisiveln2 = list()
    soman1 = 0
    soman2 = 0

    for i in range(1, n1):
        if n1 % i == 0:
            divisiveln1.append(i)

    for i in range(1, n2):
        if n2 % i == 0:
            divisiveln2.append(i)

    for i in divisiveln1:
        soman1 = soman1 + i

    for i in divisiveln2:
        soman2 = soman2 + i

    if soman1 == n2 and soman2 == n1:
        return "V"
    else:
        return "F"


def mdc(a, b, c):
    while b != 0:
        a, b = b, a % b

    while c != 0:
        a, c = c, a % c

    return a


def mmc(a, b, c):
    mdc_ab = mdc(a, b, 0)
    mmc_ab = abs(a * b) // mdc_ab

    mdc_abc = mdc(mmc_ab, c, 0)
    return abs(mmc_ab * c) // mdc_abc


def fatorial(n):
    c = n
    f = 1
    print(f"Calculando: {n}! = ", end="")
    while c > 0:
        f *= c
        c -= 1
    return f
