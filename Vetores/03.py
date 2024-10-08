tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    numero = float(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

maior = vetor[0]
menor = vetor[0]

for numero in vetor:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("O maior elemento do vetor é:", maior)
print("O menor elemento do vetor é:", menor)
