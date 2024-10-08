tamanho = int(input("Digite o tamanho da matriz (NxN): "))
matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        numero = int(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz.append(linha)

identidade = True

for i in range(tamanho):
    for j in range(tamanho):
        if i == j and matriz[i][j] != 1:
            identidade = False
        elif i != j and matriz[i][j] != 0:
            identidade = False

if identidade:
    print("A matriz é uma matriz identidade.")
else:
    print("A matriz não é uma matriz identidade.")
