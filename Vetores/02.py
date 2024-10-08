tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    numero = float(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

soma = 0

for numero in vetor:
    soma += numero

print("A soma dos elementos do vetor é:", soma)
