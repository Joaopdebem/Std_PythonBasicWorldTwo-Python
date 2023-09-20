import time

print("\n\n\nVamos verificar se você passou de ano!""\n")
print(".-." * 37)

aluno = input("\nDigite seu nome: ")
print("\nOlá, {}, vamos prosseguir com sua solicitação.".format(aluno))

def passouDeAno():
    nota1 = float(input("\nInforme a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2) / 2

    print("\nCerto {}, você tirou {:.2f} no primeiro semestre e {:.2f} no segundo semestre.".format(aluno, nota1, nota2))
    print("\nProcessando...")
    time.sleep(1.5)

    if media < 5.0:
        print("\nSua média ficou {:.2f}, infelizmente ficou abaixo de 5.0, você foi REPROVADO".format(media))
    elif media >= 7.0:
        print("\nParabéns, sua média ficou {:.2f}, você foi APROVADO".format(media))
    elif 7 > media >= 5.0:
        print("\nSua média ficou {:.2f}, ainda faltou um pouco para ser aprovado, você ficou em RECUPERAÇÃO".format(media))
        
    print("\nVocê deseja consultar novamente?"
          "\n1 - SIM"
          "\n2 - NÃO"
          "\n")
    repetir = int(input("- "))

    if repetir == 1:
        passouDeAno()
    else:
        print("\nEncerramos sua solicitação.\n")
           
passouDeAno()
