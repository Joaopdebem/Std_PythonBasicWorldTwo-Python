import time

def intervalo():
    print('-' * 220)
    print("\n\nInforme dois intervalos númericos para saber os números pares que contém entre eles!\n\n")

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    
    time.sleep(1)
    
    print("\nVocê inseriu {} e {}, entre eles estão os seguintes números pares: \n".format(numero1, numero2))
    
    if numero1 % 2 == 0:
        numero1 = numero1
    else:
        numero1 = numero1 + 1
    
    time.sleep(1.5)
    
    for i in range(numero1, numero2+1, 2):
        print(i)
    print("\n")

def loop():
    print("*" * 229)
    print("\nVocê deseja consultar outros números?"
          "\n\n1 - SIM"
          "\n2 - NÃO")
    choice = int(input("\n- "))

    if choice == 1:
        intervalo()
        loop()
    elif choice == 2:
        print("\nCerto, encerramos sua solicitação.\n\n")
    else:
        print("\nInforme uma opção válida, tente novamente.\n")
        loop()
        
intervalo()
loop()



