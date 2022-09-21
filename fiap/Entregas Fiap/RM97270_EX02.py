print("Qual o melhor dia para as lives?")
segunda = int(input("Informe a quantidade de votos para segunda-feira: "))
terca = int(input("Informe a quantidade de votos para terça-feira: "))
quarta = int(input("Informe a quantidade de votos para quarta-feira: "))
quinta = int(input("Informe a quantidade de votos para quinta-feira: "))
sexta = int(input("Informe a quantidade de votos para sexta-feira: "))
maior = segunda
if terca>maior:
    maior = terca
if quarta>maior:
    maior = quarta
if quinta > maior:
    maior = quinta
if sexta > maior:
    maior = sexta
if maior == segunda:
    print(f"O dia mais votado foi segunda-feira com {maior} votos!")
elif maior == terca:
    print(f"O dia mais votado foi terça-feira com {maior} votos!")
elif maior == quarta:
    print(f"O dia mais votado foi quarta-feira com {maior} votos!")
elif maior == quinta:
    print(f"O dia mais votado foi quinta-feira com {maior} votos!")
elif maior == sexta:
    print(f"O dia mais votado foi sexta-feira com {maior} votos!")