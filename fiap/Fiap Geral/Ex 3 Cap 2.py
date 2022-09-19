xbox = 0
nintendo = 0
playstation = 0
contador = 0
while contador < 5:
    console = int(input("Digite o número e escolha seu console: \n"
                         "1 - Xbox\n"
                         "2 - Nintendo\n"
                         "3- Playstation\n"))
    contador = contador + 1

    if console == 1:
        xbox = xbox + 1
    elif console == 2:
        nintendo = nintendo + 1
    elif console == 3:
        playstation = playstation + 1
    else:
        print("Digite um número válido!!!")
if xbox > nintendo and xbox > playstation:
    print(f"O console escolhido foi xbox com {xbox} votos")
elif nintendo > xbox and nintendo > playstation:
    print(f"O console escolhido foi o Nintendo com {nintendo} votos")
elif playstation > xbox and playstation > nintendo:
    print(f"O console escolhido foi o Playstation com {playstation} votos")
