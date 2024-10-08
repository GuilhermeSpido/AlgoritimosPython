tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    numero = float(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

for i in range(len(vetor)):
    for j in range(0, len(vetor) - i - 1):
        if vetor[j] > vetor[j + 1]:
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

print("Vetor ordenado:", vetor)
