qtd_alimentos = int(input("Informe a quantidade de alimentos consumida: "))
soma = 0
while qtd_alimentos > 0:
    calorias = int(input("Informe a quandidade de calorias do alimento: "))
    soma = soma + calorias
    qtd_alimentos = qtd_alimentos - 1
print("A quantidade da calorias total consumida foi de ",soma)
