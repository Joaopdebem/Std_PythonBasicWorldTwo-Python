import time

def main():
    print("#" * 160)
    print("\n\nInforme um número inteiro e a quantidade de elementos e lhe apresentamos sua sequência de fibonacci.\n\n")
    
    elementos = int(input("Quantos elementos mostrar: "))
    
    num1 = 0
    num2 = 1
            
    print("{} -> {}".format(num1, num2), end ="")
    cont = 3
    while cont <= elementos:
        num3 = num1 + num2    
        print(" -> {}".format(num3), end="")
        num1 = num2
        num2 = num3
        cont += 1
    print(" -> FIM")
    
    print("\n\nDeseja realizar a consulta novamente? [S/N]\n")    
    consulta = ''
    while not consulta == 'S' and  not consulta == 'N':
        consulta = str(input(""))
        consulta = consulta.upper()
        if consulta == 'S':
            print("\nRecomeçando...\n")
            time.sleep(1)
            main()
        elif consulta == 'N':
            print("\nConsulta encerrada.\n\n")
            break
        else:
            print("Opção inválida. [S/N]  Tente novamente!")
                  
main()