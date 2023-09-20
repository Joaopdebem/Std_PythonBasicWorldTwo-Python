import time

def main():
    print("*" * 225)
    print("\nInforme quantos números inteiros desejar, lhe diremos quantos números foram digitados e a soma entre eles\n\n")

    num1 = 0
    cont = 0
    soma = 0

    while num1 != 999:
        num1 = int(input("Digite um número: "))
        cont += 1
        soma += num1
        
    print("\nCom exceção do 999, você digitou {} números, a soma de todos eles é {}.".format((cont - 1), (soma - 999)))

    print("\n\nQuer começar de novo? [S/N]\n")
    consulta = ''
    
    while not consulta == 'S' and not consulta == 'N':
        consulta = str(input(""))
        consulta = consulta.upper()
        
        if consulta == 'S':
            print("\nReinciando...\n")
            time.sleep(1)
            main()
        elif consulta == 'N':
            print("\nPrograma encerrado.\n\n")
            break
        else:
            print("\nOpção inválida. [S/N]  Tente novamente!\n")
            
main()