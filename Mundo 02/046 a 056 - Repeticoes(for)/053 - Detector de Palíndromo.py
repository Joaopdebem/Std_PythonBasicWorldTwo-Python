def main():
    print("\n\nVamos verificar se a sua frase digitada é um palíndromo.")

    frase = str(input("\n\nDigite sua frase: "))

    fraseLimpa = frase.upper().replace(" ", "")
    fraseLimpaInv =  frase.upper()[::-1].replace(" ", "")

    if fraseLimpa == fraseLimpaInv:
        print('\n\nA frase "{}" é um palíndromo. Ficando assim {}.\n'.format(frase, fraseLimpaInv))
    else: 
        print("\n\nA frase {} não é um palíndromo. Fica dessa forma {}.\n".format(frase, fraseLimpaInv))
        
def loop():
    print("=-=" * 71)
    print("\n\nVocê deseja consultar outra frase?"
          "\n\n1 - SIM"
          "\n2 - NÃO\n")
    choice =  int(input(""))
    
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\nCerto então, estamos encerrando sua solicitação!")
    else:
        print("\nVocê inseriu uma opção inválida, tente novamente.")
        loop()
        
main()
loop()