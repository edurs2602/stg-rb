def calculateFibonacciNumber(verification_num):
    a, b = 0, 1

    while a <= verification_num:
        if a == verification_num:
            return print(f"O numero: {verification_num} pertece a sequencia de Fibonacci")

        a, b = b, a + b

    return print(f"O numero: {verification_num} NÃO pertece a sequencia de Fibonacci")


while True:
    try:
        user_input = int(input("- 1 função Fibonacci \n- 0 sair do programa \n Selecione uma opção: "))
    except:
        raise print("Erro ao escolher opção do usuario")

    try:
        if user_input == 0:
            print("Finalizando Programa...")
            quit()
        if user_input == 1:
            fibonacci_verification_number = int(input("Digite o numero para verificar: "))
            calculateFibonacciNumber(fibonacci_verification_number)
    except:
        raise print("Erro ao entrar na opção escolhida")
