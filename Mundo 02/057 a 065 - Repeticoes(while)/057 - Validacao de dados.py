def main():
    sexo = ''
    nomeSexo = ''
    
    while not sexo == 'M' and not sexo == 'F':
        sexo = str(input("\nDigite seu sexo [M/F]: ")).upper()
        print("\nSexo inválido, tente novamente.")
    
    if sexo == 'M':
        nomeSexo = 'Masculino'
    else:
        nomeSexo = 'Feminino'

    print("\nO sexo informado é {}\n".format(nomeSexo))
    
def loop():
    print("#" * 200)
    print("\nDeseja fazer uma nova consulta?"
          "\n\nDigite 1 - para SIM"
          "\nDigite 2 - para NÃO\n")
    
    choice = int(input(""))

    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\nConsulta finalizada. Obrigado!\n\n")
        
    else:
        print("\nOpção inválida. Tente novamente")
        loop()

main()
loop()