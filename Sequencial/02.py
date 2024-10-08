N = int(input("Quantos números você deseja inserir? "))
soma = 0

for i in range(N):
    numero = float(input(f"Digite o número {i + 1}: "))
    soma += numero

media = soma / N
print("A média aritmética dos números inseridos é:", media)
