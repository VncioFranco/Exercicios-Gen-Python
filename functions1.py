def somar():
    num1=float(input("digite o primeiro número da soma:"))
    num2=float(input("digite o segundo número da soma:"))
    soma = num1+num2
    print("A soma dos dois números digitados é",soma)


def subtrair():
   num1=int(input("digite o primeiro número da subtração:"))
   num2=int(input("digite o segundo número da subtração:"))
   subtrai = num1-num2
   print("A subtração",num1,"-",num2,"é igual a:",subtrai)


def dividir():
    num1=float(input("digite o primeiro número da divisão:"))
    num2=float(input("digite o segundo número da divisão:"))
    if(num2 == 0):
        print("Não é possivel dividir por 0")
        return
    else:
        divisao = num1 / num2
        print("A divisão",num1,"/",num2,"é igual a:",divisao)


def multiplicar():
    num1=float(input("digite o primeiro número da multiplicação:"))
    num2=float(input("digite o segundo número da multiplicação:"))
    multiplica= num1*num2

    print("A multiplicação de",num1,"X",num2,"é igual a:",multiplica)


print("Bem vindo a sua Calculadora desenvolvida em Python!")

continuar = "s"

while continuar.lower() =="s":
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")

    op=input("Escolhau ma opção: ")

    match op:
        case "1":
            somar()
        case "2":
            subtrair()
        case "3":
            dividir()
        case "4":
            multiplicar()
        case _:
            print("opção invalida!")


    continuar = input("\nDeseja realizar outra operação? (s/n): ")

print("Calculadora encerrada!")




