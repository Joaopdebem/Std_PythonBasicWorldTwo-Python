import time

def main():
    print("\n\n\nVamos fazer uma progressão aritmética!\n\n")

    primeiroNum = int(input("Insira o número da progressão: "))
    razao = int(input("Insira a razão: "))
    elementos = int(input("Quantos elementos? "))

    ultimoNum = primeiroNum + (elementos - 1) * razao
    ultimoNum += 1

    print("\n\nFoi informado o número {}, a razão {} e {} elementos.".format(primeiroNum, razao, elementos))
    time.sleep(2)
    print("\n\nAguardando cálculo de sua progressão aritmética...\n\n")
    time.sleep(2)
    
    for i in range(primeiroNum, ultimoNum, razao):
        print(i)
    
def loop():
    print("\n\nVocê deseja realizar uma nova consulta?"
          "\n\n1 - SIM"
          "\n2 - NÃO\n")
    choice = int(input(" "))
    
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\nCerto! Estamos encerrando sua solicitação!\n\n")
    else:
        print("\nInsira uma opção válida.")
        loop()

main()
loop()

