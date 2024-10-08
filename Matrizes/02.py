linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = int(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz.append(linha)

matriz_transposta = []

for j in range(colunas):
    linha_transposta = []
    for i in range(linhas):
        linha_transposta.append(matriz[i][j])
    matriz_transposta.append(linha_transposta)

print("A matriz transposta é:")
for linha in matriz_transposta:
    print(linha)
