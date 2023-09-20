import time

def main():
    print("\n\nVamos calcular a soma de todos números ímpares que são múltiplos de três entre dois valores.\n\n")
    
    primeiroValor = int(input("Informe o primeiro valor: "))
    segundoValor = int(input("Informe o segundo valor: "))
    
    if (primeiroValor % 2) != 0 or primeiroValor == 1:
        print("\nCerto, vamos prosseguir.")
        primeiroValorImpar = primeiroValor
    else:
        primeiroValorImpar = primeiroValor + 1
        print("\nCerto, vamos prosseguir.")
    
    somar = 0
    for numero in range((primeiroValorImpar), (segundoValor + 1), 2):
        if numero % 3 == 0 and numero % 2 != 0:
            somar += numero
    time.sleep(1)
    print("\n\nA soma de todos os números ímpares que são múltiplos de três entre {} e {} é: {}".format(primeiroValor, segundoValor, somar))

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

