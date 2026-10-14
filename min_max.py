def min_max(numeros):
    return min(numeros), max(numeros)

menor, maior = min_max([4, 9, 1, 7])
print(maior, menor)

resultado = min_max([4, 9, 1, 7])
print(resultado)
print(type(resultado))