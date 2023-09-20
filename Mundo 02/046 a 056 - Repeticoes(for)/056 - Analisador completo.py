def main():
    numPessoas = int(input("\n\nInforme a quantidade de pessoas que deseja inserir os dados: "))
    
    somaIdade = 0
    mediaIdade = 0
    maiorIdadeHomem = 0
    nomeVelho = ''
    totalMulher20 = 0
    
    for person in range(1, (numPessoas + 1)):
        nome = str(input("\n\nInforme o nome da {}º pessoa: ".format(person))).strip()
        idade = int(input("Informe a idade da {}º pessoa: ".format(person)))
        sexo = str(input("Informe o sexo da {}º pessoa, com 'M' para masculino e 'F' para feminino: ".format(person))).strip()
        somaIdade += idade

        if person == 1 and sexo in 'Mm':
            maiorIdadeHomem = idade
            nomeVelho = nome 
        
        if sexo in 'Mm' and idade > maiorIdadeHomem:
            maiorIdadeHomem = idade
            nomeVelho = nome
            
        if sexo in 'Ff' and idade < 20:
            totalMulher20 += 1
            
                       
    mediaIdade = somaIdade / numPessoas   
    
    print("\n\nA média de idade do grupo é de {} anos".format(mediaIdade))
    print("O homem mais velho se chama {} e tem {} anos.".format(nomeVelho, maiorIdadeHomem))
    print("Nesse grupo tem {} mulher(es) com menos de 20 anos.".format(totalMulher20))
       
def loop():
    print("\n\nDeseja realizar uma nova consulta?"
          "\n\nDigite 1 - para SIM"
          "\nDigite 2 - para NÃO\n")
    choice = int(input(" "))
    
    if choice == 1:
        main()
        loop()
    elif choice == 2:
        print("\nO programa foi finalizado. Obrigado!\n")
        print("¨" * 170)
    else:
        print("\nOpção inválida. Tente novamente.")
        loop()
      
main()
loop()



        