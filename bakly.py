menu = """
      ------- MENU -------
          Bem vindo(a)!
    
   Pressione a tecla referente 
   à ação que deseja realizar:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)


    if opcao == "d":

            valor = float(input("Digite o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("\nDepósito realizado com sucesso! \nO valor já encontra-se em sua conta.")

            else:
                print("A operação falhou! O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input(f"\nInforme o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES



        if excedeu_saldo:
            print("A operação falhou! Não há saldo suficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("A operação falhou! O número máximo de saques foi atingido.")

        elif valor > 0:

              saldo -= valor
              extrato += f"Saque: R$ {valor:.2f}\n"
              numero_saques += 1
              print(f"Saque realizado com sucesso!\nPor favor, retire o seu dinheiro.") 


        else:
             print("A operação falhou! O valor informado é inválido.")


    elif opcao == "e":
            print("\n ============ EXTRATO ============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===================================")

    elif opcao == "q":
            break

    else: 
            print("Operação inválida, por favor tente novamente selecionando a opção desejada.")