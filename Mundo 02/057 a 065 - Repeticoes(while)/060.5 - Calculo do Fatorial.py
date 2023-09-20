import time

def main():
    print("\n\nInforme um número para calcular seu fatorial.\n")

    num1 = int(input("Digite um número: "))
    num2 = num1
    fatorial = 1

    print("\nCalculando a fatorial de {}...\n".format(num1))
    time.sleep(1.5)
    
    while num2 > 0:
        print("{} ".format(num2), end="")
        print("-> " if num2 > 1 else " = ", end="")
        fatorial *= num2
        num2 -= 1
    print("{}".format(fatorial))
     
    print("\nDeseja saber o fatorial de outro número? [S/N]\n")
    novaConsulta = 0
    
    while novaConsulta != 'S' and novaConsulta != 'N':
        novaConsulta = str(input(""))
        novaConsulta = novaConsulta.upper()
        if novaConsulta == 'S':
            main()
        elif novaConsulta == 'N':
            print("\nConsulta encerrada!\n\n")
            break
        else:
            print("Opção inválida[S/N]. Tente novamente!")
     
main()