import time

def main():
    print("#" * 210)
    print("\n\nIremos identificar o maior e menor peso informado.")
    
    pessoas = int(input("\n\nInsira a quantidade de pessoas a qual vai informar o peso: "))
    time.sleep(1)
    print("\nOk. A seguir você irá informar o peso de {} pessoas. Vamos começar.\n\n".format(pessoas))
    
    listPesos = []
    
    for i in range(1, (pessoas + 1)):
        peso = float(input("Insira o peso da {}º pessoa em KGs: ".format(i)))
        listPesos.append(peso)

    listPesos.sort()    
        
    print("\n\nDas {} pessoas informadas, o maior peso é {} KG e o menor foi {} KG.\n\n".format(pessoas, listPesos[-1], listPesos[0]))
    print("#" * 210)

def loop():
    print("\n\nVamos realizar uma nova consulta?"
          "\n\n1 - SIM"
          "\n2 - NÃO\n")
    choice =  int(input(""))
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\nSolicitação encerrada. Obrigado.\n\n")
    else:
        print("*" * 210)
        print("Opção inválida. Tente novamente.")    
        print("*" * 210)
        loop()
    


main()
loop()