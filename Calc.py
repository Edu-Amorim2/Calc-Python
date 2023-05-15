#Calculadora de Valores Inteiros - @Edu-Amorim2
while True:
    print("Calculadora Básica")

    def Add():
        print("Escolhido Adição")
        valor1 = int(input("Coloque o Primeiro Valor:"))
        valor2 = int(input("coloque o Segundo Valor:"))
        result = print("O Resultado é igual à" , valor1 + valor2)
      
    def Subs():
        print("Escolhido Substração")
        valor1 = int(input("Coloque o Primeiro Valor: "))
        valor2 = int(input("coloque o Segundo Valor:"))
        result = print("O Resultado é igual à" , valor1 - valor2)
        
    def Mult():
        print("Escolhido Multiplicação")
        valor1 = int(input("Coloque o Primeiro Valor: "))
        valor2 = int(input("coloque o Segundo Valor:"))
        result = print("O Resultado é igual à" , valor1 * valor2)

    def Divs():
        print("Escolhido Divisão")
        valor1 = int(input("Coloque o Primeiro Valor: "))
        valor2 = int(input("coloque o Segundo Valor:"))
        result = print("O Resultado é igual à" , valor1 / valor2)

    def Err():
        print("Programa Encerrado")
        
        
        
    print("Escolha o Tipo de Conta: \n 1 - Adição \n 2 - Substração \n 3 - Multiplicação \n 4 - Divisão\n 5- Fim")


    a = int(input("Digite Aqui:"))

    if a == 1:
        Add()
        
    if a == 2:
        Subs()
        
    if a == 3:
        Mult()
        
    if a == 4:
        Divs()
    
    if a == 5:
        Err()
        break