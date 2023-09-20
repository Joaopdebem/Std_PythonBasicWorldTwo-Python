def main():
    print("\n\n\nVamos checar quanto ficou sua compra!""\n")
    print("¬-¬" * 37)
    global produto
    produto = float(input("\nInforme o valor total de seus produtos: R$"))
    print("\nO total de sua compra deu R${:.2f}, Qual seria seu método de pagamento?".format(produto))    

def formaDePagamento():
    pagamento = int(input("\n1 - A vista dinheiro (10% de desconto)"
                      "\n2 - A vista cartão (5% de desconto)"
                      "\n3 - Em até 2x no cartão"
                      "\n4 - 3x ou mais (20% de juros)"
                      "\n"))

    if pagamento == 1:  
        avistaDinheiro = produto - (produto * 0.10)
        print("\nVocê optou por pagar a vista no dinheiro, com o desconto suas compras ficam R${:.2f}.".format(avistaDinheiro), "\n")
    elif pagamento == 2:    
        avistaCartao = produto - (produto * 0.05)
        print("\nVocê optou por pagar a vista no cartão, com o desconto, suas compras ficam R${:.2f}.".format(avistaCartao), "\n")
    elif pagamento == 3:    
        print("\nVocê optou por parcelar em 2x, suas parcelas ficam no valor de RS{:.2f}, com o total da compra de RS{:.2f}.".format((produto / 2), produto), "\n")
    elif pagamento == 4:    
        comJuros = produto + (produto * 0.2)
        print("\nVocê optou por parcelar em 3x ou mais, com os juros, o total de sua compra fica RS{:.2f}, e suas parcelas partem de RS{:.2f}.".format(comJuros, (comJuros / 3), "\n"))
    else:
        print("\nVocê digitou uma forma de pagamento inválida"
              "\nTente novamente.")
        formaDePagamento()
        
def rep():
    print("\nVocê deseja simular um novo valor?"
          "\n1 - Sim"
          "\n2 - Não")
    voltar = int(input("- "))
    
    if voltar == 1:
        main()
        formaDePagamento()
        rep()
    elif voltar == 2:
        print("\nEncerramos sua solicitação\n\n")
    else:
        print("Escolha uma opção válida.")
        rep()
    
main()
formaDePagamento()
rep()