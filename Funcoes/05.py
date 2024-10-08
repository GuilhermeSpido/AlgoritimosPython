def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"O máximo divisor comum entre {num1} e {num2} é: {mdc(num1, num2)}")
