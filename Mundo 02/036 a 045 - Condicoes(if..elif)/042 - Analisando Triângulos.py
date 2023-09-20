import time

print("\n\n\nInforme o comprimento de 3 retas para saber o que será formado\n")
print("*-" *55)

def triangulo():
    reta1 = int(input("\nDigite a primeira reta em metros: "))
    reta2 = int(input("Digite a segunda reta em metros: "))
    reta3 = int(input("Digite a terceira reta em metros: "))

    print("\nProcessando...")
    time.sleep(1)

    if reta1 == reta2 == reta3:
        print("\nComo todos lados são iguais a {}m. Formou um triângulo equilátero.".format(reta1), "\n")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("\nSendo as três retas {}m, {}m e {}m, e duas delas são iguais, forma um triângulo Isósceles.".format(reta1, reta2, reta3), "\n")
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print("\nCom as três retas {}m, {}m e {}m. Todas possuem medidas diferentes, formando um Triângulo Escaleno.".format(reta1, reta2, reta3), "\n")
    time.sleep(1)
    
def rep():
    print("Deseja fazer uma nova consulta?"
          "\n1 - SIM"
          "\n2 - NÃO"
          "\n")
    consulta = int(input("- "))
    time.sleep(1)
    
    if consulta == 1:
        triangulo()
        rep()
    elif consulta == 2:
        print("\nEncerramos sua solicitação.\n\n")
    else:
        print("\nEscolha uma opção válida.\n")
        rep()
        
triangulo()
rep()    
    
