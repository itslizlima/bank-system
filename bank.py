def menu(): 
    menu = """

      ------- MENU -------

          Bem vindo(a)!
    
   Pressione a tecla referente 
   à ação que deseja realizar:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Abrir conta
    [c] Fechar conta
    [l] Listar contas
    [u] Novo usuário
    [q] Sair

> """

    return input(menu)

def  depositar(saldo, valor, extrato, /):

     if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso! \nO valor já encontra-se em sua conta.")
            
     else:
        print("A operação falhou! O valor informado é inválido.")

     return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        
        
        
        if excedeu_saldo:
            print("\nA operação falhou! Não há saldo suficiente.")

        elif excedeu_limite:
            print("\nA operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nA operação falhou! O número máximo de saques foi atingido.")

        elif valor > 0:
              
              saldo -= valor
              extrato += f"Saque: R$ {valor:.2f}\n"
              numero_saques += 1
              print(f"Saque realizado com sucesso!\nPor favor, retire o seu dinheiro.") 
        
        
        else:
             print("\nA operação falhou! O valor informado é inválido.")

        return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
            print("\n ============ EXTRATO ============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===================================")

def criar_usuario(usuarios):
      cpf = input("Informe o seu CPF (somente números): ")
      usuario = filtrar_usuario(cpf, usuarios)

      if usuario:
            print("\n Esse CPF já está em utilização!")
            return
      nome = input("\nInforme o seu nome completo: ")
      data_nascimento = input("\n Informe a sua data de nascimento (dd-mm-aaaa): ")
      endereco = input("\nInforme o seu endereço seguindo os requisitos: (logradouro, num - bairro - cidade/sigla do estado): ")

      usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

      print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

      return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
      cpf = input("\nPor favor, informe o seu CPF: ")
      usuario = filtrar_usuario(cpf, usuarios)

      if usuario:
            print("\nA sua conta foi criada com sucesso! ")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

            print("\nUsuário não encontrado, o processo de criação de conta foi interrompido.")

def excluir_conta(agencia, numero_conta, usuarios):
      cpf = input("\nPor favor, informe o seu CPF: ")
      usuario = filtrar_usuario(cpf, usuarios)

      if usuario:
            print("\nO processo de fechamento da sua conta foi concluído. ")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listar_contas(contas):
      for conta in contas:
            linha = f"""\
                Agência:\t{conta["agencia"]}
                C/C:\t\t{conta["numero_conta"]}
                Titular:\t{conta["usuario"]["nome"]}
                """
            print("=" * 100)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
    
        if opcao == "d":

            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":

            valor = float(input(f"\nInforme o valor do saque: "))

            saldo, extrato = sacar(
                  saldo=saldo,
                  valor=valor,
                  extrato=extrato,
                  limite=limite,
                  numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES,
    
            )

        elif opcao == "e":
              exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
              criar_usuario(usuarios)

        elif opcao == "n":
              numero_conta = len(contas) + 1
              conta = criar_conta(AGENCIA, numero_conta, usuarios)

              if conta:
                    contas.append(conta)

        elif opcao == "c":
              numero_conta = len(contas) - 1
              conta = excluir_conta(AGENCIA, numero_conta, usuarios)

              if conta:
                    contas.remove(conta)
                    print("Lamentamos que tenha fechado a sua conta... Mas agradecemos seu tempo conosco!")
        
        elif opcao == "l":
              listar_contas(contas)

        elif opcao == "q":
            break

        else: 
            print("Operação inválida, por favor tente novamente selecionando a opção desejada.")
