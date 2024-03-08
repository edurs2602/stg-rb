def invertString(string):
    inverted_char = []

    for char in string:
        inverted_char.insert(0, char)

    inverted_string = ''.join(inverted_char)

    return print(f"Sua string era: {string} e invertida ficou da seguinte forma: {inverted_string}")


while True:
    try:
        user_input = int(input("- 1 função Inverter String \n- 0 sair do programa \n Selecione uma opção: "))
    except:
        raise print("Erro ao escolher opção do usuario")

    try:
        if user_input == 0:
            print("Finalizando Programa...")
            quit()
        if user_input == 1:
            string_for_invert = input("Digite uma string para inverter: ")
            invertString(string_for_invert)
    except:
        raise print("Erro ao entrar na opção escolhida")
