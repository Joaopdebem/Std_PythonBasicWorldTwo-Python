import time

print("Vamos calcular seu IMC!""\n")
print("-_-" * 37)

def calculo():
    peso = float(input("\nDigite seu peso em KG: "))
    altura = float(input("Digite sua altura em Metros: "))
    imc = peso / (altura * altura)
    print("\nVocê possuí {:.1f}KG e {:.2f}m".format(peso, altura))

    print("Processando...")
    time.sleep(1.5)

    if imc < 18.5:
        print("\nSeu IMC deu {:.2f}, você está abaixo do peso.".format(imc),"\n")
    elif imc >= 18.5 and imc < 25:
        print("\nSeu IMC deu {:.2f}, você está no seu peso ideal.".format(imc),"\n")
    elif imc >= 25 and imc < 30:
        print("\nSeu IMC deu {:.2f}, você está com sobrepeso.".format(imc),"\n")
    elif imc >= 30 and imc < 40:
        print("\nSeu IMC deu {:.2f}, você está com obesidade.".format(imc),"\n")
    else:
        print("\nSeu IMC deu {:.2f}, você está com obesidade mórbida.".format(imc),"\n")
        
    print("Você deseja realizar o cálculo novamente?")
    
    rep = int(input("\n1 - Para sim"
                    "\n2 - Para não"
                    "\n"))
    if rep == 1:
        calculo()
    else:
        print("Certo, sua solicitação foi encerrada.")

calculo()