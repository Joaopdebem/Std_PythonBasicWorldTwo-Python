import random
import time

print("\n\n\nOlá, vamos jogar Pedra, Papel Tesoura!""\n")
print("°-°" * 32)

def jogo():
    print("\nDigite o número de acordo com sua escolha.\n")
    escolhaJogador = int(input("\n1 - Pedra"
                        "\n2 - Papel"
                        "\n3 - Tesoura"
                        "\n\n"))
    escolhaPC = random.choice([1, 2, 3])

    if escolhaJogador == 1 or escolhaJogador == 2 or escolhaJogador == 3:
        print("\nVamos jogar!\n")
    else:
        print("Escolha entre uma das opções, tente novamente.\n")
        print("-_-" * 32)
        jogo()
        
    if escolhaJogador == 1:
        escolhaJogador = "Pedra"
    elif escolhaJogador == 2:
        escolhaJogador = "Papel"
    else:
        escolhaJogador = "Tesoura"
        
    if escolhaPC == 1:
        escolhaPC = "Pedra"
    elif escolhaPC == 2:
        escolhaPC = "Papel"
    elif escolhaPC == 3:
        escolhaPC = "Tesoura"
    
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO\n")
    time.sleep(2)
    
    if escolhaJogador == escolhaPC:
        print("EMPATE!.")
    elif escolhaJogador == "Pedra" and escolhaPC == "Papel" or escolhaJogador == "Papel" and escolhaPC == "Tesoura" or escolhaJogador == "Tesoura" and escolhaPC == "Pedra":
        print("EU GANHEI")
    else:
        print("VOCÊ GANHOU")
        
    print("Jogador jogou {}, computador jogou {}.".format(escolhaJogador, escolhaPC))
        
    time.sleep(1.5)
    
def retornar():
    print("\nQuer tentar novamente?")
    print("\n1 - SIM"
          "\n2 - NÃO")
    novamente = int(input("- "))
    
    if novamente == 1:
        jogo()
        retornar()
    elif novamente == 2:
        print("Jogo encerrado, obrigado pela disputa!\n")
    else:
        print("Tente uma opção válida.\n")
        retornar()

jogo()
retornar()