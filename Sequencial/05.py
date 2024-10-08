N = int(input("Quantos números da sequência de Fibonacci você deseja gerar? "))
fibonacci = [0, 1]

for i in range(2, N):
    proximo_numero = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo_numero)

print("Os primeiros", N, "números da sequência de Fibonacci são:")
for numero in fibonacci[:N]:
    print(numero, end=" ")
print()
