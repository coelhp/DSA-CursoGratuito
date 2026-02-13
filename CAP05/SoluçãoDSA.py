# Estudo de Caso 2 - Lógica de Programação - Fundamentos de Linguagem Python Para Construção de Game

# --- 1. Apresentação e Regras ---

# Usamos a função print() para exibir mensagens na tela (Saída Padrão).
print("-"*30)
print("--- Jogo Pedra, Papel e Tesoura (2 Jogadores) ---")
print("-"*30)
print("Bem-vindos! Cada jogador deve escolher uma das opções.")

# Usamos uma tupla para armazenar as opções válidas.
# Tuplas são boas aqui porque as opções do jogo não mudam (são imutáveis).
opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("-" * 25) # Imprime uma linha para separar

# --- 2. Coleta dos Dados de Entrada ---

# Usamos a função input() para receber o que o usuário digita (Entrada Padrão).
# A função input() sempre retorna uma string.
jogada_jogador1_inicial = input("Jogador 1, digite sua jogada: ")
jogada_jogador2_inicial = input("Jogador 2, digite sua jogada: ")

# --- 3. Tratamento dos Dados de Entrada ---

# Manipulação de Strings: usamos .lower() para converter para minúsculas
# e .strip() para remover espaços extras. Isso evita erros como "Pedra" != "pedra".
jogada_jogador1 = jogada_jogador1_inicial.lower().strip()
jogada_jogador2 = jogada_jogador2_inicial.lower().strip()

print("-" * 25)
print(f"Jogador 1 escolheu: {jogada_jogador1}")
print(f"Jogador 2 escolheu: {jogada_jogador2}")
print("-" * 25)

# --- 4. Lógica do Jogo e Resultado ---

# Primeiro, verificamos se as jogadas são válidas.
# Há várias opções para checar se a jogada está dentro da nossa tupla de opções.

if jogada_jogador1 not in opcoes_validas or jogada_jogador2 not in opcoes_validas:
#if opcoes_validas.count(jogada_jogador1) == 0 or opcoes_validas.count(jogada_jogador2) == 0:
#if {jogada_jogador1, jogada_jogador2} - set(opcoes_validas):
#if not all(jogada in opcoes_validas for jogada in [jogada_jogador1, jogada_jogador2]):
#if len(list(filter(lambda x: x not in opcoes_validas, [jogada_jogador1, jogada_jogador2]))) > 0:
    print("DSA: Uma ou ambas as jogadas são inválidas! Por favor, use apenas 'pedra', 'papel' ou 'tesoura'.")

# Agora, a lógica principal do jogo, usando operadores de comparação (==) e lógicos (and, or).

# Caso 1: Empate
elif jogada_jogador1 == jogada_jogador2:
    print("Resultado: É um empate!")

# Caso 2: Jogador 1 vence
# Agrupamos todas as condições de vitória do Jogador 1 com o operador 'or'.
elif (jogada_jogador1 == "pedra" and jogada_jogador2 == "tesoura") or \
     (jogada_jogador1 == "tesoura" and jogada_jogador2 == "papel") or \
     (jogada_jogador1 == "papel" and jogada_jogador2 == "pedra"):
    print("Resultado: Jogador 1 venceu! Parabéns!")

# Caso 3: Se não empatou e o Jogador 1 não venceu, então o Jogador 2 venceu.
else:
    print("Resultado: Jogador 2 venceu! Parabéns!")


print("\n--- Fim de Jogo ---")
