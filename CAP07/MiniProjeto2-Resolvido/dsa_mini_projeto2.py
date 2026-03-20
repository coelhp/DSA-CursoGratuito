"""
Módulo principal da aplicação de sistema bancário digital, implementando a interface de usuário e o fluxo de operações.
"""

# Importando a classe Banco responsável pelo gerenciamento de clientes e contas
from dsaoperacoes.banco import Banco

# Importando exceções personalizadas para uso no fluxo de operações
from dsautilitarios.exceptions import SaldoInsuficienteError, ContaInexistenteError

# Definindo função para exibir o menu principal da aplicação
def menu_principal():

    print("\n--- DSA Mini-Projeto 2 - Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")

    # Retornando a opção recebida do usuário
    return input("Escolha uma opção: ")

# Definindo função que exibe o menu de operações de uma conta específica
def menu_conta(banco):

    try:

        # Solicitando ao usuário o número de sua conta
        num_conta = int(input("Digite o número da conta: "))

        # Buscando a conta no banco; Aqui há possibilidade de gerar exceção se não existir
        conta = banco.buscar_conta(num_conta)
        
        # Abrindo loop de operações dentro da conta
        while True:

            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")
            
            # Lendo a opção escolhida pelo usuário
            opcao = input("Escolha uma opção: ")

            if opcao == '1':

                # Depositando valor na conta definida
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            
            elif opcao == '2':
                
                # Tentativa de realizar um saque
                try:
                    
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)  # Demonstrativo de polimorfismo: depende do tipo de conta
                
                except SaldoInsuficienteError as e:
                    print(f"Erro na operação: {e}")
            
            elif opcao == '3':
                
                # Exibindo o extrato da conta do usuário
                conta.extrato()
            
            elif opcao == '4':
                
                # Saindo do menu da conta e retornando ao menu principal
                break
            
            else:
                print("Opção inválida. Tente novamente mais tarde.")

    # Exceção para caso a conta não exista
    except ContaInexistenteError as e:
        print(f"Erro: {e}")
    
    # Exceção para entradas inválidas (ex: valores não numéricos)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número válido.")

# Definindo função principal que faz o controle do fluxo do sistema
def main():
    
    # Criando o objeto Banco que irá gerenciar clientes e contas
    banco = Banco("Banco Digital PRSC")

    # Abrindo o loop principal do sistema
    while True:

        opcao = menu_principal()

        if opcao == '1':
            
            # Adicionando um novo cliente ao cadastro do banco
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome, cpf)
        
        elif opcao == '2':
            
            # Criando uma nova conta vinculada a um cliente já existente
            cpf = input("Digite o CPF do cliente para vincular a conta: ")
            cliente = banco._clientes.get(cpf)
            
            if cliente:

                tipo = input("Digite o tipo da conta (corrente/poupanca): ")
                banco.criar_conta(cliente, tipo)
            
            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")

        elif opcao == '3':

            # Abrindo o menu de operações de uma conta específica, onde o usuário pode depositar, sacar ou ver o extrato
            menu_conta(banco)
            
        elif opcao == '4':

            # Encerrando o programa com mensagem de despedida.
            print("\nObrigado por usar o nosso sistema. Até logo!\n")
            break
        
        else:

            print("\nOpção inválida. Por favor, tente novamente.\n")

# Ponto de entrada da aplicação.
if __name__ == "__main__":
    main()





