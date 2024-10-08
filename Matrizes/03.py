linhas = int(input("Digite o número de linhas das matrizes: "))
colunas = int(input("Digite o número de colunas das matrizes: "))
matriz1 = []
matriz2 = []

print("Preencha a primeira matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = int(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz1.append(linha)

print("Preencha a segunda matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = int(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz2.append(linha)

matriz_soma = []

for i in range(linhas):
    linha_soma = []
    for j in range(colunas):
        linha_soma.append(matriz1[i][j] + matriz2[i][j])
    matriz_soma.append(linha_soma)

print("A soma das matrizes é:")
for linha in matriz_soma:
    print(linha)
