def main():
    print("\n\nVamos verificar se o número digitado é primo.")
    
    num = int(input("\n\nInsira um número: "))

    if num > 1:
        for i in range(1, num):
            if num % i != 0:
                print("\n\n", num, "- É um número primo.")
            else:
                print("\n\n", num, "- Não é um número primo.")        
                break
    else:
        print("\nVocê inseriu {}, é um número inválido, insira um número POSITIVO, diferente de 0 e 1.".format(num), "\n")
        print("-_-" * 76)
        main()
        
def loop():
    print("\n\nVocê deseja consultar outro número?"
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