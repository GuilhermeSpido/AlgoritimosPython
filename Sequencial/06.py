N = int(input("Quantos números você deseja inserir? "))
numeros = []

for i in range(N):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Números em ordem crescente:")
for numero in numeros:
    print(numero, end=" ")
print()
