"""
Exceções customizadas para a aplicação de sistema bancário.
"""

# Definindo a exceção personalizada para saldo insuficiente ao tentar sacar
class SaldoInsuficienteError(Exception):

    """
    Exceção criada para quando uma operação de saque excede o saldo disponível.
    """

    # Construtor para exceção
    def __init__(self, saldo_atual, valor_saque, mensagem="Saldo insuficiente para efetuar o saque."):
        
        # Saldo da conta no momento da tentativa de saque
        self.saldo_atual = saldo_atual
        
        # Valor da tentativa de saque
        self.valor_saque = valor_saque
        
        # Mensagem detalhada, explicando o motivo do erro e mostrando o saldo atual e o valor que se tentou sacar
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f}, Tentativa de saque: R${valor_saque:.2f}"
        
        # Chamando o construtor da classe Exception e printando a mensagem
        super().__init__(self.mensagem)

# Definindo a exceção personalizada para operações em contas inexistentes
class ContaInexistenteError(Exception):
    
    """
    Exceção criada para quando o usuárrio tentar operar em uma conta que não existe.
    """
    
    # Construtor de exceção
    def __init__(self, numero_conta, mensagem="A conta solicitada não foi encontrada."):
        
        # Número identificador da conta que se tentou acessar
        self.numero_conta = numero_conta
        
        # Mensagem detalhada, explicando o motivo do erro e mostrando o número da conta que se tentou acessar
        self.mensagem = f"{mensagem} Número da conta: {numero_conta}"
        
        # Chamando o construtor da classe Exception e printando a mensagem
        super().__init__(self.mensagem)
