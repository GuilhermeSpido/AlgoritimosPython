N = int(input("Digite um número inteiro não negativo N: "))
fatorial = 1

if N < 0:
    print("Fatorial não é definido para números negativos.")
else:
    for i in range(1, N + 1):
        fatorial *= i

print("O fatorial de", N, "é:", fatorial)
