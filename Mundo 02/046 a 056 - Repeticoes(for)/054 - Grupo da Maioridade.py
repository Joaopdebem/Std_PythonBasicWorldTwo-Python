import time
import datetime

def main():
    print("¨¨¨" * 70)
    print("\n\nNesse programa você irá informar quantas datas deseja consultar, e ele lhe retornará quantas atingiram maioridade e quantas que não.\n\n")
    
    contMaior = 0
    contMenor = 0
    anoAtual = datetime.date.today().year
    
    listAnoNasc = []
    elementos = int(input("Quantas datas você quer inserir?  "))
    time.sleep(1.5)
    print("\n\nCerto, iremos consultar {} datas, podemos começar.\n".format(elementos))

    for i in range(1, (elementos + 1)):
        anoNasc = int(input("Ano de nascimento da {}º pessoa: ".format(i)))
        if anoAtual - anoNasc >= 18:    
            contMaior += 1
        else:
            contMenor += 1
        listAnoNasc.append(anoNasc)

    listAnoNasc.sort()
    time.sleep(1.5)
    print("\n\nTemos datas desde {} até {}, dentre essas {} atingiram a maioridade e {} ainda não.".format(listAnoNasc[0], listAnoNasc[-1], contMaior, contMenor),"\n\n")
    print("¨¨¨" * 70)
    time.sleep(1)

def loop():
    print("\n\nDesejar realizar uma nova consulta?"
          "\n\n1 - SIM"
          "\n2 - NÃO\n")
    choice = int(input(""))
    print("\n\n")
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("Sua solicitação foi encerrada. Obrigado.\n\n")
    else:
        print("Você inseriu uma opção inválida. Tente novamente.\n")
        loop()
        
main()
loop()