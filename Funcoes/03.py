def media_lista(lista):
    soma = sum(lista)
    return soma / len(lista)

tamanho = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(tamanho):
    numero = float(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

print(f"A média da lista é: {media_lista(lista):.2f}")
