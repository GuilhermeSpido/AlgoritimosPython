tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    numero = int(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

elemento = int(input("Digite o elemento a ser contado: "))
contagem = 0

for numero in vetor:
    if numero == elemento:
        contagem += 1

print(f"O elemento {elemento} aparece {contagem} vezes no vetor.")
