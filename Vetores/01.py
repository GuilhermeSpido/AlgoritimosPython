tamanho = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(tamanho):
    numero = int(input(f"Digite o número {i + 1}: "))
    lista.append(numero)

lista_invertida = []

for i in range(tamanho - 1, -1, -1):
    lista_invertida.append(lista[i])

print("Lista original:", lista)
print("Lista invertida:", lista_invertida)
