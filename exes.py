def destobin(x):
    if x == 0:
        return 0
    y = ""
    while x > 0:
        z = x % 2
        y += str(z)
    return y[::-1]
x = int(input())
print(destobin(x))
def delenie(x):
    y = ""
    while x > 0:
