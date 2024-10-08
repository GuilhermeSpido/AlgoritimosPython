linhas_a = int(input("Digite o número de linhas da matriz A: "))
colunas_a = int(input("Digite o número de colunas da matriz A: "))
matriz_a = []

for i in range(linhas_a):
    linha = []
    for j in range(colunas_a):
        numero = int(input(f"Digite o elemento A[{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz_a.append(linha)

linhas_b = int(input("Digite o número de linhas da matriz B: "))
colunas_b = int(input("Digite o número de colunas da matriz B: "))

if colunas_a != linhas_b:
    print("As matrizes não podem ser multiplicadas.")
else:
    matriz_b = []
    for i in range(linhas_b):
        linha = []
        for j in range(colunas_b):
            numero = int(input(f"Digite o elemento B[{i + 1}][{j + 1}]: "))
            linha.append(numero)
        matriz_b.append(linha)

    matriz_resultado = []
    for i in range(linhas_a):
        linha_resultado = []
        for j in range(colunas_b):
            soma = 0
            for k in range(colunas_a):
                soma += matriz_a[i][k] * matriz_b[k][j]
            linha_resultado.append(soma)
        matriz_resultado.append(linha_resultado)

    print("O resultado da multiplicação das matrizes é:")
    for linha in matriz_resultado:
        print(linha)
