import time

print("\n\n\nVamos converter um número de sua escolha.\n")
print("-=-" * 31)
numero = int(input("\nDigite um número: "))
time.sleep(1)
print("\nVocê digitou {}. Para o que você deseja converter?".format(numero))

def menu():
    print("\n[1] Binário"
      "\n[2] Octal"
      "\n[3] Hexadecimal")
    converter = input("- ")
    print("\n...\n")
    time.sleep(1)
    if converter == "1":
        print("O número {} em binário é {}.".format(numero, bin(numero)[2:]),
              "\n")
    elif converter == "2":
        print("O número {} em octal é {}.".format(numero, oct(numero)[2:]),
              "\n")
    elif converter == "3":
        print("O número {} em hexadecimal é {}.".format(numero, hex(numero)[2:]),
              "\n")
    else:
        print("Opção inválida.")
        menu()



menu()
loop()