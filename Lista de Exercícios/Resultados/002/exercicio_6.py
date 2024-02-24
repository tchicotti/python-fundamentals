# Exercício 6: Solicite ao usuário dois números e peça que solicite uma operação matemática (+, -, *, /). Depois de receber a operação matemática escolhida, exibir o resultado.
# Após exibir o resultado, perguntar ao usuário se deseja realizar um novo cálculo.
# Se a resposta for S reinicie a operação, se for N encerre o programa. Caso não seja nem S ou N, informar que a escolha foi inválida.

while True:
    num_1 = float(input("Informe o primeiro número: "))
    num_2 = float(input("Informe o segundo número: "))
    operacao = input("Informe a operação matemática desejada (+, -, *, /): ")

    if operacao in ['+', '-', '*', '/']:
        resultado = None
        if operacao == '+':
            resultado = num_1 + num_2
        elif operacao == '-':
            resultado = num_1 - num_2
        elif operacao == '*':
            resultado = num_1 * num_2
        # elif operacao == '/':
        else:
            if num_2 == 0:
                print("Não é possível dividir por zero")
            else:
                resultado = num_1 / num_2
                
        if resultado != None:
            print(f"A operação de {num_1} {operacao} {num_2} = {resultado}")
        
        while True:
            resposta = input("Deseja realizar um novo cálculo? (S - sim) (N - não)").lower()
            
            if resposta in ['s','n']:
                break
            else:
                print("Opção inválida. Informe corretamente S para sim ou N para sair do programa")
            
        if resposta == 'n':
            break
    else:
        print("Operação solicitada inválida, tente novamente. \n")
    
