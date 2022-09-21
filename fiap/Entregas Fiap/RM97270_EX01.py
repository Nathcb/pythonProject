plano = input("Informe o seu tipo de assinatura: ")
faturamento = float(input("Informe o seu faturamento anual: "))
if plano.lower() == "basic":
    bonus = faturamento * 0.3
    print(f"O valor do bônus a ser pago é de {bonus}")
elif plano.lower() == "silver":
    bonus = faturamento * 0.2
    print(f"O valor do bônus a ser pago é de {bonus}")
elif plano.lower() == "gold":
    bonus = faturamento * 0.1
    print(f"O valor do bônus a ser pago é de {bonus}")
elif plano.lower() == "platinum":
    bonus = faturamento * 0.05
    print(f"O valor do bônus a ser pago é de {bonus}")
else:
    print("Por favor, digite um plano válido!")