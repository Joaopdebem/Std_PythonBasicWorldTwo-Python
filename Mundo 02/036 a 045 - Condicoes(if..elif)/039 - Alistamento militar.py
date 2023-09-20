print("\n\n\nVamos verificar como está seu status com o serviço militar!""\n\n")

idade = int(input("Digite sua idade: "))

def aniv():
    global aniversario 
    aniversario = int(input("\nVocê faz aniversário esse ano?"
                        "\n1 - Sim"
                        "\n2 - Não"
                        "\n- "))
    if aniversario != 1 and aniversario != 2:
        aniv()  

if idade == 18 or idade == 17:
    aniv()

if idade == 18 and aniversario == 2 or idade == 17 and aniversario == 1:
    print("\nVocê está no ano de seu alistamento. Procure a junte militar mais próxima para se informar.\n")
elif idade < 18 or idade == 17 and aniversario == 2:
    print("\nAinda não chegou seu momento de se alistar, falta aproximadamente {} anos, continue acompanhando.".format(18 - idade), "\n") 
elif idade > 18 or idade == 18 and aniversario == 1:
    print("\nVocê provavelmente já passou dos 18 ou faz aniversário esse ano, seu tempo de alistamento já passou, foi aproximadamente a {} ano(s), procure uma junta militar para ficar em dia com o serviço militar.".format(idade - 18), "\n")



