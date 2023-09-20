import time

print("Para seguir sua solicitação de empréstimo precisamos das seguintes informações:")

valorCasa = float(input("Digite o valor da casa em reais: "))
salarioComprador = float(input("Digite o salário do comprador: "))
tempoPagamento = int(input("Quantos anos você planeja pagar o empréstimo? "))
prestacaoCasa = valorCasa / (tempoPagamento * 12)
time.sleep(1)
print("A prestação da casa ficou R${:.2f} mensalmente.".format(prestacaoCasa))
print("Aguarde um momento...")
time.sleep(2)
if prestacaoCasa <= (salarioComprador * 0.30):
    print("Seu empréstimo foi aceito com uma parcela de R${:.2f}.".format(prestacaoCasa))
else:
    print("Seu empréstimo foi negado.")

