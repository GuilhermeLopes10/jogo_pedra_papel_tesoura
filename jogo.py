import random

def pedra_papel_tesoura():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    opcoes = ["pedra", "papel", "tesoura"]
    
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        
        if jogador == "sair":
            print("Obrigado por jogar! Até a próxima!")
            break
        
        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue
        
        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
        else:
            print("Você perdeu!")
        print()

# Executa o jogo
pedra_papel_tesoura()
