def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

quantidade = int(input("Digite o número de elementos da sequência de Fibonacci: "))
print(f"A sequência de Fibonacci com {quantidade} elementos é: {fibonacci(quantidade)}")
