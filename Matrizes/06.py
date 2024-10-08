linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = float(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz.append(linha)

for i in range(linhas):
    soma = 0
    for j in range(colunas):
        soma += matriz[i][j]
    media = soma / colunas
    print(f"A média da linha {i + 1} é: {media:.2f}")
