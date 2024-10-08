renda = float(input("Digite sua renda anual: "))

if renda <= 22847.76:
    print("Isento de Imposto de Renda.")
elif renda <= 33919.80:
    imposto = renda * 0.15
    print(f"Imposto a pagar: R${imposto:.2f}")
else:
    imposto = renda * 0.275
    print(f"Imposto a pagar: R${imposto:.2f}")
