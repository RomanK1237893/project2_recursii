def nok(a, b):
    nok.mult = nok.mult + b
    if ((nok.mult % a == 0) and (nok.mult % b == 0)):
        return nok.mult
    else:
        nok(a, b)
    return nok.mult

def nod(a, b):
    if (b == 0):
        return a
    else:
        return nod(b, a % b)

nok.mult = 0
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
NOD = nod(a, b)
if (a > b):
    NOK = nok(b, a)
else:
    NOK = nok(a, b)
print("НОК:")
print(NOK)
print("НОД: ")
print(NOD)