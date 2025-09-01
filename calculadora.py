# Função calculadoura
def calculadora():
    # inicia um loop com opçoes para o usuario digitar
    while True:
        print("\n=== CALCULADORA SIMPLES ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")
        
        # variavel que armazena o que o usuario digitou
        opcao = input("Escolha uma opção: ")

        # se o que o usuario digitou for o numero 5 o código para
        if opcao == "5":
            print("Encerrando a calculadora...")
            break
        
        try:
            # esse variavel pede para o usuario digitar armazena o primeiro numero digitado
            num1 = float(input("Digite o primeiro número: "))
            # esse variavel pede para o usuario digitar armazena o segundo numero digitado
            num2 = float(input("Digite o segundo número: "))

            # esse bloco se o usuario digitar uma opção que nao conta na lista informa opção invalida e retora ao menu novamente
        except ValueError:
            print("⚠️ Entrada inválida, digite apenas números!")
            continue

        # esse bloco de if e else seleciona a operação a ser feita
        # identifica a opção 1 soma o num1 + o num2 e mostra na tela
        if opcao == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")

        # identifica a opção 2 subitrai o num1 - o num2 e mostra na tela
        elif opcao == "2":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")

        # identifica a opção 3 multiplica o num1 * o num2 e mostra na tela
        elif opcao == "3":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")

        # identifica a opção 4 verifica se o numero digitado é zero se nao for  divide o num1 / o num2 e mostra na tela
        elif opcao == "4":
            if num2 == 0:
                print("⚠️ Erro: divisão por zero não é permitida!")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("⚠️ Opção inválida! Tente novamente.")

# Executar a calculadora
calculadora()
