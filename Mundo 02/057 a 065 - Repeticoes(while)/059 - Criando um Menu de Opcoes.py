import time

def main():
    print("\n\nInsira dois números!\n")

    num1 = 0
    num2 = 0 
    numOption = 0
    soma = 0
    multi = 0 
    maior = 0

    while not numOption == 5:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        time.sleep(1)    
        print("\nVocê digitou {} e {}, o que você deseja fazer com eles?".format(num1, num2))
        print("\n\n[1] Somar"
            "\n[2] Multiplicar"
            "\n[3] Maior"
            "\n[4] Novos números"
            "\n[5] Sair do programa\n")
        numOption = int(input(""))
        
        if numOption == 1:
            soma = num1 + num2
            print("\n\nVocê decidiu somar, a somas dos dois números é {}.".format(soma))
            print("\nDeseja recomeçar o programa? [S/N]\n")
            renew = str(input(""))
            renew = renew.upper()
            if renew == 'S':
                numOption = 4
            elif renew == 'N':
                numOption = 5
            else:
                print("Você inseriu uma opcão inválida. O programa irá recomecar.")
                
        if numOption == 2:
            multi = num1 * num2
            print("\n\nVocê decidiu multiplicar. O resultado da multiplicação é {}.".format(multi))
            print("\nDeseja recomeçar o programa? [S/N]\n")
            renew = str(input(""))
            renew = renew.upper()
            if renew == 'S':
                numOption = 4
            elif renew == 'N':
                numOption = 5
            else:
                print("Você inseriu uma opcão inválida. O programa irá recomecar.")
                 
        if numOption == 3:            
            if num1 < num2:
                maior = num2
            else:
                maior = num1
            print("\n\nO maior número entre eles é {}.".format(maior))
            print("\nDeseja recomeçar o programa? [S/N]\n")
            renew = str(input(""))
            renew = renew.upper()
            if renew == 'S':
                numOption = 4
            elif renew == 'N':
                numOption = 5
            else:
                print("Você inseriu uma opcão inválida. O programa irá recomecar.")
                
        if numOption == 4:
            main()
            
        if numOption == 5:
            print("\n\nPrograma encerrado.\n")
            print("-=-" * 76)
            break
        
main()