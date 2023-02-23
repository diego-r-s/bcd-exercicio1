num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um segundo número inteiro: "))
escolha = int(input("Escolha uma operação a ser realizada ( 1= + ,2= - ,3= * ,4= / ): "))

valor_soma = num1 + num2
valor_sub = num1 - num2
valor_mult = num1 * num2
valor_div = num1/num2

if escolha == 1:
    print("O valor final será de: %.2f " %valor_soma)
if escolha == 2:
    print("O valor final será de: %.2f " %valor_sub)
if escolha == 3:
    print("O valor final será de: %.2f " %valor_mult)
if escolha == 4:
    print("O valor final será de: %.2f " %valor_div)
