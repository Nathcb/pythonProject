val_pct = int(input("Informe o valor do pacote: "))
ctg_assentos = input("Informe a categoria dos assentos: ")
qtd_passageiros = int(input("Informe a quantidade de passageiros que residem na mesma casa: "))
if qtd_passageiros == 2 and ctg_assentos.lower() == "economica":
    val_liq = val_pct * 0.97
    val_med = val_liq/qtd_passageiros
    print(f"O valor da sua viagem é de {val_pct}\n"
          f"O seu DESCONTO é de 3%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros == 3 and ctg_assentos.lower() == "economica":
    val_liq = val_pct * 0.96
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 4%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros >= 4 and ctg_assentos.lower() == "economica":
    val_liq = val_pct * 0.95
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 5%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros == 2 and ctg_assentos.lower() == "executiva":
    val_liq = val_pct * 0.95
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 5%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros == 3 and ctg_assentos.lower() == "executiva":
    val_liq = val_pct * 0.93
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 7%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros >= 4 and ctg_assentos.lower() == "executiva":
    val_liq = val_pct * 0.92
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 8%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros == 2 and ctg_assentos.lower() == "primeira classe":
    val_liq = val_pct * 0.90
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 10%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros == 3 and ctg_assentos.lower() == "primeira classe":
    val_liq = val_pct * 0.85
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 15%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
elif qtd_passageiros >= 4 and ctg_assentos.lower() == "primeira classe":
    val_liq = val_pct * 0.8
    val_med = val_liq/qtd_passageiros
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"O seu DESCONTO é de 20%\n"
          f"O valor líquido da sua viagem é de {val_liq}\n"
          f"O valor médio por viajante é de {val_med}")
else:
    print(f"O valor bruto da sua viajem é de {val_pct}\n"
          f"VOCÊ NÃO POSSUI DESCONTO!!!\n"
          f"O valor líquido da sua viagem é de {val_pct}\n"
          f"O valor médio por viajante é de {val_pct/qtd_passageiros}")