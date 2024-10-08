import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 5

print("Adivinhe o número entre 1 e 100. Você tem 5 tentativas.")

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break
else:
    print(f"Você não adivinhou o número. O número era {numero_secreto}.")
