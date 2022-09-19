fibonnaci = 0
n1 = 0
n2 = 1
entrada = int(input("Digite um número: "))
while fibonnaci != entrada:
    fibonnaci = n1 + n2
    n1 = n2
    n2 = fibonnaci
    if entrada == fibonnaci:
        print("Ação bem sucedida!")
        break
    elif fibonnaci > entrada:
        print("A ação falhou . . .")
        break