menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_depositado = float(input("Quanto quer depositar: "))
        if valor_depositado <= 0:
            print("Erro! Depositar um valor positivo!")
        else:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print("Valor depositado com sucesso!")


    elif opcao == "s":
        print("Saque")
        valor_do_saque = float(input("Quanto deseja sacar: "))
        if numero_saque == LIMITE_SAQUE:
            print("Limite de saque por dia atingindo!") 
        elif valor_do_saque > 500:
            print("Limite máximo de 500 reais. Tente novamente!")
        elif saldo < valor_do_saque:
            print("Saldo insuficiente!")
        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            extrato += f"Saque: R$ {valor_do_saque:.2f}\n"
            numero_saque += 1
            print("Sucesso!")
        else:
            print("Erro na operação! O valor é inválido!")     

    elif opcao == "e":
        print("\n=============Extrato=============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")


    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")