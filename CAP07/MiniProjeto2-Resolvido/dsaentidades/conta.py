"""
Módulo que define as classes de conta (Abstrata, Corrente e Poupança)    
"""

from abc import ABC, abstractmethod # -> Classe abstrata e decorador para métodos abstratos
from datetime import datetime # -> Datetime para registro temporal das transações
from dsautilitarios.exceptions import SaldoInsuficienteError # -> Exceção personalizada para saldo insuficiente

# Definindo a classe abstrata Conta, que será base para outros tipos
class Conta(ABC):
    """
    Classe com base abstrata para contas bancárias
    Demonstrativos de herança e encapsulamento
    """
    
    _total_contas = 0
    
    # Construtor
    def __init__(self, numero: int, cliente):
        
        self.numero = numero # -> Número da conta (atr. protegido)
        self.saldo = 0.0 #-> Saldo da conta, inicializado em 0 (atr. protegido)
        self.cliente = cliente
        self.historico = []
        
        Conta._total_contas += 1
    
    
    @property # Property para acessar o saldo de forma controlada
    def saldo(self):
        """
        Método getter para o saldo, controlando o acesso
        """
        
        return self.saldo
    
    @classmethod # Método para consulta do número total de contas
    def get_total_contas(cls):
        """
        Método da classe para obter a qtd. total de contas criadas
        """
        
        return cls._total_contas
    
    def depositar(self, valor: float): # Método para depósitos
        
        if valor > 0:
            
            self.saldo += valor
            self.historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            
        else:
            
            print("Valor de depósito inválido.")
            
    @abstractmethod #-> Método abstrato que deve ser implementado pelas subclasses
    def sacar(self, valor: float):
        """
        Método para sacara um valor
        Deve ser implementado pelas subclasses
        """
        pass
    
    def extrato(self):
        """
        Exibe o extrato da conta.
        """
        
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R${self._saldo:.2f}")
        print("Histórico de transações:") 
        
        print("-"*30)       
        
        if not self.historico: # Verifica caso não haja transações registradas
            print("Não há registros de transações no período.")
            
        for data, transacao in self.historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}")
        print("-"*30)
        
# Definindo a subclasse ContaCorrente
class ContaCorrente(Conta):
    """
    Subclasse para conta corrente
    Representando polimorfismo ao sobrescrever o método sacar.
    """
    
    def __init__(self, numero: int, cliente, limite: float = 500.0):
        
        super().__init__(numero, cliente) # -> Chamando construtor da classe
        self.limite = limite # -> Definindo o limite do cheque especial
        
    def sacar(self, valor: float): # Implementação do método com cheque especial
        """
        Permite que o usuário saque utilizando o saldo da conta mais o limite de cheque especial.
        """

        if valor <= 0:
            print("Valor de saque indisponível!")
            return
        
        # Calculando o saldo disponível somado ao limite
        saldo_disponivel = self.saldo + self.limite

        # Se o valor do saque ultrapassar o saldo disponível
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")

        # Realizando dedução do valor do saque do saldo
        self._saldo -= saldo

        # Armazenando a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso")

# Criando a subclasse ContaPoupanca
class ContaPoupanca(Conta):

    """
    Representa a conta poupança
    """

    # Construtor da poupança, herda construtor base
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    # Implementação do método sacar apenas com saldo disponível
    def sacar(self, valor: float):

        # Valida e permite o saque caso o saldo seja suficiente
        if valor <= 0:
            print("Valor de saque impossível no momento, verifique seu saldo!")
            return

        # Verifica se há saldo suficiente
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)

        # Realizando dedução do valor do saque do saldo
        self._saldo -= saldo

        # Armazenando a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso")
