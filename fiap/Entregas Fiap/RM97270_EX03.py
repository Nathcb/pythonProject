total_pares = 0
total_impares = 0
for impares in range(1,50,2):
    impares = int(input("VOCÊ ESTÁ DIGITANDO A NOTA DOS ALUNOS ÍMPARES \n"
                        f"Por favor digite a nota do aluno {impares}: "))
    total_impares = impares + total_impares
for pares in range(1,50,2):
    pares = int(input(f"VOCÊ ESTÁ DIGITANDO A NOTA DOS ALUNOS PARES \n"
                      f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {pares+1}: "))
    total_pares = pares + total_pares
media_impares = total_impares/25
print(f"A média das notas dos alunos ímpares é de {media_impares}")
media_pares = total_pares/25
print(f"A média das notas dos alunos pares é de {media_pares}")
if media_pares > media_impares:
    print(f"A metade de sala que teve a maior média foi a de alunos pares, com média de {media_pares}.")
elif media_impares > media_pares:
    print(f"A metade da sala que teve a menor média foi a de alunos ímpares, com média de {media_impares}.")
else:
    print(f"As médias das duas metades da sala foram iguais.")
