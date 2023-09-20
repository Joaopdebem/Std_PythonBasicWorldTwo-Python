import time

def main():
    print("\n\nVamos lhe apresentar a tabuada do número desejado!\n\n")
    
    numero = input("\nDigite o número: ")
    print("\nCalculando...\n")
    time.sleep(1.5)

    for i in range(1, 11):
        print("{} x {} = {}".format(numero, i, int(numero)*i))

def loop():
    print("\n\nVocê deseja consultar novamente?"
          "\n\n1 - SIM"
          "\n2 - NÃO\n")
    choice = int(input(""))
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\n\nCerto, estamos finalizando sua solicitação.\n\n")
    else:
        print("\n\nVocê inseriu uma opção inválida, tente novamente.")
        loop()

main()
loop()