def potencia(base, expoente=2):
    return base ** expoente

n = int(input("nummero:"))
e = input("expoente(enter = 2):") or 2
if e == "":
    print(potencia(n))
else:
    print(potencia(n, int(e)))