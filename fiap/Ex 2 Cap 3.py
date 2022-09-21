trns = int(input("Informe quantas trasações foram realizadas no dia: "))
media = trns
total = 0
while trns > 0:
    value = float(input("Informe o valor da transação: "))
    total = total + value
    trns = trns - 1
media1 = total/media
print(f"O valor total gasto foi de {total}\n"
      f"A media de valor gasto por transação foi de {media1}")