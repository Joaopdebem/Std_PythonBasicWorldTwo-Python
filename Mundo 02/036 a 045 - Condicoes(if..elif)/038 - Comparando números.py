print("\n\n\nInforme dois números e lhe diremos o maior deles.""\n")
print("-=-" * 37)

numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("\nO primeiro número, {}, é maior que o segundo, {}.".format(numero1, numero2), "\n")
elif numero2 > numero1:
    print("\nO segundo número, {}, é maior que o primeiro, {}.".format(numero2, numero1), "\n")
else:
    print("\nAmbos números são iguais não tem um maior.\n")