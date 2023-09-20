import math

def main():
    print("\n\nInforme um número para calcular seu fatorial.\n")

    num1 = int(input("Digite um número: "))
    num1 = math.factorial(num1)

    print("\nSeu número em fatorial fica {}\n\n".format(num1))
    print("-=-" * 76)
    print("\nDeseja fazer uma nova consulta? [S/N]\n")
    consulta = 0
    
    while not consulta == 'S' or not consulta == 'N':
        consulta = str(input("Insira sua resposta: "))
        consulta = consulta.upper()
        if consulta == 'S':
            main()
        elif consulta == 'N':
            print("\nConsulta encerrada.")
            break
        else:
            print("\nVocê inseriu uma opcão inválida. Tente novamente")
            
main()