tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    numero = int(input(f"Digite o número {i + 1}: "))
    vetor.append(numero)

vetor_sem_duplicatas = []

for numero in vetor:
    if numero not in vetor_sem_duplicatas:
        vetor_sem_duplicatas.append(numero)

print("Vetor original:", vetor)
print("Vetor sem duplicatas:", vetor_sem_duplicatas)
