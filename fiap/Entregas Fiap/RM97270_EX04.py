minutos = int(input("Informe os minutos atuais para encontrar a senha: "))
fatorial = 1
i = 2
while i <= minutos:
    fatorial = fatorial * i
    i = i + 1

print(f"A senha para o desbloqueio é LIBERDADE{fatorial}")