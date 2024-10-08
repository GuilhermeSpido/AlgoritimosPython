N = int(input("Digite um número inteiro N: "))
is_primo = True

if N <= 1:
    is_primo = False
else:
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            is_primo = False
            break

if is_primo:
    print(N, "é um número primo.")
else:
    print(N, "não é um número primo.")
