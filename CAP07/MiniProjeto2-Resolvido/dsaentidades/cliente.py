"""
Criando módulo da entidade do Cliente
"""

# Definindo a classe cliente

class Cliente:
    
    # Construtor que inicializa os atributos da classe
    def __init__(self, nome: str, cpf: str):
        
        self.nome = nome
        self.cpf = cpf
        self.contas = []
        
    # Construtor para adicionar uma conta a lista de contas do usuário
    def adicionar_conta(self, conta):
        
        self.contas.append(conta)
        
    # Método para definir a repsentação em string do objeto
    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"