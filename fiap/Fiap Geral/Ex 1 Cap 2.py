batimentos = int(input("Informe o valor de seus batimentos por minuto: "))
idade = int(input("Informe a sua idade: "))

if idade >= 2 and batimentos >= 120 and batimentos <= 140:
    print("Frequência cardíaca normal")
elif idade >= 2 and idade <= 17 and batimentos >= 80 and batimentos <= 100:
    print("Frequência cardíaca normal")
elif idade >= 18 and idade <= 61 and batimentos >= 70 and batimentos <= 80:
    print("Frequência cardíaca normal")
elif idade >= 60 and batimentos >= 50 and batimentos <= 60:
    print("Frenquência cardíaca normal")
else:
    print("Frequência cardíaca alterada")