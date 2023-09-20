import time

def main():
    
    print("=" * 186)
    print("\n\nCalculadora de Progressão Aritmética 2.0\n\n")
    
    primeiroTermo = int(input("Digite o primeiro termo: "))
    razao = int(input("Informe a razão: "))
    numElementos = int(input("Quantos elementos na progressão? "))

    elemento = primeiroTermo
    cont = 1
    
    print("\nA progressão aritmética irá começar com {}, e tem a razão {}, também foi definido {} termos a serem apresentados.".format(primeiroTermo, razao, numElementos))
    print("\nTrazendo resultados...\n")
    time.sleep(1.5)

    while cont <= numElementos:
        print('{} - '.format(elemento), end='')
        elemento += razao
        cont += 1
        if cont > numElementos:
            print("\n\nDeseja consultar quantos termos a mais? \n")
            novosElementos = int(input(""))
            if novosElementos == 0:
                print("\nVocê informou {} termos. Sua solicitação foi encerrada.".format(novosElementos))
                break
            print("\nCalculando...\n\n")
            time.sleep(1)
            numElementos = numElementos + novosElementos
        
    print("\nPrograma finalizado.\n")
    
main()