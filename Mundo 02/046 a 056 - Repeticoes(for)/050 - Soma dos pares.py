def main():
    print("\n\nInforme seis valores para saber a soma deles.\n\n")

    somar = 0
    contar = 0

    for i in range(1, 7):
        num = int(input("{}º valor: ".format(i)))
        if num % 2 == 0:
            num1 = num
            somar += num1
            contar += 1
        else:
            num2 = num


    print("\n\nVocê informou {} números, ignorando os ímpars, a soma foi {}.\n\n".format(contar, somar))
    
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