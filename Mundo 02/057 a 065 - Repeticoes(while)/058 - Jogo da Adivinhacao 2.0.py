import random
import time

def main():
    print("-_-" * 40)
    print("\nBem vindo ao jogo de avinhação 2.0\n")
    print("-_-" * 40)
    
    numRandom = random.randint(0, 10)
    numDigitado = 0
        
    print("\nO computador já escolheu seu número, tente adivinhar.\n\n")
    
    while not numDigitado == numRandom:
        numDigitado = int(input("Seu palpite: "))
        if numDigitado == numRandom:
            break
        else:
            print("Errou! Tente novamente.\n")
            
    print("\nVocê acertou! O computador escolheu {} e você também escolheu {}.\n".format(numRandom, numDigitado))

    print("Deseja jogar novamente?"
          "\n\n[S / N]\n")
    
    choice = 0

    while not choice == 'S' or choice == 'N':
        choice = str(input("")).upper()
        if choice == 'S':
            print("Iremos recomeçar o jogo!")
            time.sleep(1.5)
            main()
        elif choice == 'N':
            print("\nJogo encerrado!\n\n")
            break
        else:
            print("\nVocê digitou uma opção inválida. Tente novamente! [S/N]\n")

main()
