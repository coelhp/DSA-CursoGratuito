# Módulo que define a classe principal do Banco, que gerencia clientes e contas.

from dsaentidades.cliente import Cliente # -> Classe Cliente
from dsaentidades.conta import Conta, ContaCorrente, ContaPoupanca # -> Classes Base Conta e subclasses Corrente e Poupança
from dsautilitarios.exceptions import ContaInexistenteError # -> Exceção Personalizada para conta inexistente

# Definindo classe banco
class Banco:

    """
    Gerenciamento de operações do banco
    Demonstrativo de composição, pois "tem" clientes e contas
    """

    # Método Construtor da classe Banco
    def __init__(self, nome: str):

        self.nome = nome # -> Nome do banco

        self._clientes = {} # -> Dicionário de Clientes {chave: CPF, valor: objeto Cliente}

        self._contas = {} # -> Dicionário de Contas {chave: número da cotna, valor: objeto Conta}

    # Método para adicionar um novo cliente ao banco
    def adicionar_cliente(self, nome: str, cpf: str) -> Cliente:

        """
        Cria e adiciona um novo cliente ao banco.
        """

        # Valida se o cpf já está cadastrado.
        if cpf in self._clientes:
            print("Erro: Este CPF já está cadastrado")
            return self._clientes[cpf]

        # Cria o Cliente e adiciona ao dicionário
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} foi adicionado com êxito")
        
        return novo_cliente

    # Método para criar uma conta para o cliente
    def criar_conta(self, cliente: Cliente, tipo: str) -> Conta:

        """
        Cria uma nova conta para um cliente existente
        """

        # Número novo de contas baseado no total de contas +1
        numero_conta = Conta.get_total_contas() + 1

        # Método pra criar conta corrente se o tipo for solicitado
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta, cliente)

        # Cria conta poupança se for solicitada
        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)

        # Caso o tipo não seja válido
        else:
            print("Tipo de conta inválido, defina entre conta corrente ou conta poupança")
            
            return None

        # Adicionando conta ao dicionário
        self._contas[numero_conta] = nova_conta

        # Associa conta e cliente
        cliente.adicionar_conta(nova_conta)

        print(f"Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}")

    # Método de busca por número de conta
    def buscar_conta(self, numero_conta: int) -> Conta:

        """
        Busca uma conta pelo número
        """

        # Tenta recuperar a conta do dicionário
        conta = self._contas.get(numero_conta)

        # Caso não encontre, lança exceção personalizada
        if not conta:
            raise ContaInexistenteError(numero_conta)
        
        return conta