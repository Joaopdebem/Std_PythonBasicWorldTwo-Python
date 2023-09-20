
def main():
    continuar = 'S'
    num1 = 0
    soma = 0
    listaNum = []
    cont = 0
    menor = 0
    maior = 0
    media = 0
    
    print("\n\nDigite quantos números quiser. Iremos lhe dizer quantos foram digitados, a média, o maior e menor valor digitado.\n\n")
    
    while continuar == 'S':
        num1 = int(input("Digite um número: "))
        listaNum.append(num1)
        soma = soma + num1
        print("\nVocê quer continuar? [S/N]\n")
        continuar = str(input(""))
        continuar = continuar.upper()
        if continuar != 'S':
            listaNum.sort()
            cont = len(listaNum)
            menor = listaNum[0]
            maior = listaNum[-1]
            media = soma / cont
            print("\n\nConsulta encerrada! Foram digitados {} números.".format(cont))
            print("Sendo o maior {}, e o menor {}, com uma média de {}.\n\n".format(maior, menor, media))
            break

main() 