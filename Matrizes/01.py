linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = int(input(f"Digite o elemento [{i + 1}][{j + 1}]: "))
        linha.append(numero)
    matriz.append(linha)

print("A matriz é:")
for linha in matriz:
    print(linha)
