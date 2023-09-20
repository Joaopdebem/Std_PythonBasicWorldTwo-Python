import time
import datetime

print("\n\n\nVamos verificar a qual categoria o atleta pertence.""\n\n")

def categoria():
    nome = input("Digite o nome do atleta: ")
    nascimento = int(input("Digite o ano de seu nascimento: "))
    
    idade = datetime.datetime.now().year - nascimento
    
    print("\nCarregando...""\n")
    time.sleep(2)

    if idade <= 9:
        print("Atleta {}, possui {} anos e pertence a categoria Mirim.".format(nome, idade))
    elif idade > 9 and idade <= 14:
        print("Atleta {}, possui {} anos e pertence a categoria Infantil.".format(nome, idade))
    elif idade > 14 and idade <= 19:
        print("Atleta {}, possui {} anos e pertence a categoria Junior.".format(nome, idade))
    elif idade == 20:
        print("Atleta {}, possui {} anos e pertence a categoria Senior.".format(nome, idade))
    else:
        print("Atleta {}, possui {} anos e pertence a categoria Master.".format(nome, idade))
    
    print("\nVocê deseja consultar sobre outro atleta?")
    rep = int(input("\n1 - Sim"
                    "\n2 - Não"
                    "\n- "))
    if rep == 1:
        categoria()
    else:
        print("\nEncerramos sua solicitação!\n")
    
categoria()