import time

def main():
    print("=-" * 114)
    print("\n\nPodemos iniciar a contagenm dos fogos de artifício?\n\n")
    resposta = int(input("1 - SIM"
                         "\n2 - NÃO\n"
                         "\nInsira sua resposta: "))
    time.sleep(1)

    if resposta == 1:
        time.sleep(2)
        print("\nDaremos inicio a contagem."
              "\n")
        for i in range(10, 0, -1):
            print(i)
            time.sleep(1)
        time.sleep(1)
        print("\n\nFeliz ano novo!!\n\n")
        time.sleep(2.5)
    elif resposta == 2:
        print("\n\nCerto, estamos encerrando sua solicitação. Obrigado!!")
    else:
        print("\n\nPor gentileza, selecione uma opção válida. Tente novamente.\n")
        main()

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