agenda = []


def novo():
    global agenda
    nome = p_nome()
    celular = input("Celular: ")
    email = input("E-mail: ")
    agenda.append([nome, celular, email])
    print(""
          "-----------------------\n"
          "Registro gravado com sucesso!!!\n"
          "-----------------------\n")


def p_nome():
    return input("Nome: ")


def listar_dados(nome, celular, email):
    print("Nome: %s \n"
          "Celular: %s \n"
          "Email: %s \n" % (nome, celular, email))
    print("-------------------------")


def listar():
    print(""
          "CONTATOS DA AGENDA"
          "")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
        print(""
              "FIM DA AGENDA"
              "")


def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda):
        if e[0].lower() == name:
            return d
        return None


def pesquisar():
    p = pesquisa(p_nome())
    if p != None:
        print("Registro encontrado!\n")
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        listar_dados(nome, celular, email)
    else:
        print("\n"
              "Nome não encontrado!!!\n")


def apagar():
    global agenda
    nome = p_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
        print("\n"
              "-------------------------\n"
              "Registro APAGADO com sucesso!!!\n"
              "")
    else:
        print("Nome não encontrado")


def editar():
    p = pesquisa(p_nome())
    if p != None:
        nome = agenda[p][0]
        print("Nome: ", nome)
        celular = input("Celular: ")
        email = input("E-mail: ")
        agenda[p] = [nome, celular, email]
        print("\n"
              "---------------------------\n"
              "Registro EDITADO com sucesso!!!\n"
              "\n"
              )
    else:
        print("Nome não encontrado")


def validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
            else:
                return 0
        except ValueError:
            print("Valor inválido,favor digitar entre %d e %d " % (inicio, fim))


def menu():
    print(""
          "1 - Adicionar novo contato\n"
          "2 - Editar um contato\n"
          "3 - Pesquisar contato\n"
          "4 - Lista de contatos\n"
          "5 - Apagar um contato\n"
          "6 - Sair")
    return validar("Ecolha uma opção: ", 1, 6)

while True:
    opcao = menu()
    if opcao == 0:
        print("Opção Inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()
