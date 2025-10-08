def tres_maiores(numeros: list[int]):
    return sorted(numeros, reverse=True)[:3]

lista = [10, 25, 400, 98, 2, 45, 39]
resultado = tres_maiores(lista)
print(resultado)
