nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f"A média é {media:.2f}. Aluno aprovado.")
elif media >= 5:
    print(f"A média é {media:.2f}. Aluno em recuperação.")
else:
    print(f"A média é {media:.2f}. Aluno reprovado.")
