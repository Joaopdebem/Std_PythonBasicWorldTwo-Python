import time

def main():
    
    print("¬" * 226)
    print("\n\nCalculadora de Progressão Aritmética 2.0\n\n")
    
    
    primeiroTermo = int(input("Digite o primeiro termo da progressão: "))
    razao = int(input("Informe a razão da progressão: "))
    numTermos = int(input("Informe a quantidade de termos a ser apresentado: "))

    termo = primeiroTermo
    cont = 1
    
    print("\nO primeiro termo informado foi {}, com a razão {}, e foi definido {} termos a serem impressos na tela.".format(primeiroTermo, razao, numTermos))
    print("\nCalculando...\n\n")
    time.sleep(1.5)

    while cont <= numTermos:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print("Fim")
    
    print("\n\nDeseja fazer uma nova consulta? [S/N]\n")
    novaConsulta = 0
    
    while not novaConsulta == 'S' or novaConsulta =='N':
        novaConsulta = str(input(""))
        novaConsulta = novaConsulta.upper()
        
        if novaConsulta == 'S':
            main()
        elif novaConsulta == 'N':
            print("\nSolicitação encerrada.\n\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
    
main()