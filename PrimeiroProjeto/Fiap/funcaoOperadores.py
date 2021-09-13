print("==== INICIO DO PROGRAMA ====")

programa = int(input("Vamos iniciar?  1 - sim | 2 - nao:  "))

while programa == 1:
    
    escolha = int(
    input("Escolha uma operação: 1 - somar | 2 - subtrair | 3 - multiplicar | 4 - dividir  "))
    
    if(escolha > 0 and escolha < 5) :
    
        primeiroNumero = int(input("Primeiro número: "))
        segundoNumero = int(input("Segundo número: "))

        def somar():
            soma = primeiroNumero + segundoNumero
            print("A soma é", soma)


        def subtrair():
            subtracao = primeiroNumero - segundoNumero
            print("A diferença é", subtracao)


        def multiplicar():
            multiplicacao = primeiroNumero * segundoNumero
            print("O produto é", multiplicacao)


        def dividir():
            divisao = primeiroNumero / segundoNumero
            print("O quociente é", divisao)


        if(escolha == 1):
            somar()
        elif(escolha == 2):
            subtrair()
        elif(escolha == 3):
            multiplicar()
        elif(escolha == 4):
            dividir()
    else :
        print("OPERAÇÃO INEXISTENTE")
    
    programa = int(input("Deseja contiuar?  1 - sim | 2 - nao "))

print("==== FIM DO PROGRAMA ====")
