# Exercício 7: Você está criando um sistema que irá calcular quanto um cinema recebe por sessão do filme que está em cartaz "As tranças do Rei Careca". 
# Você deve solicitar que seja informado:
# - qual a capacidade de assentos de uma sala do cinema,
# - o valor do Ingresso Inteiro, 
# - o valor do Meio-Ingresso, 
# - quantas vendas foram realizadas daquela sessão
# - das vendas realizadas quantas foram Inteiros 
# - quantas foram Meio-Ingresso.

# Você deve exibir:
# Qual a porcentagem de assentos vendidos.
# Qual a porcentagem de assentos vendidos como Ingresso Inteiro.
# Qual a porcentagem de assentos vendidos como Meio-Ingresso.
# Exibir qual o total de vendas por tipo de ingresso.
# Exibir o total da receita por sessão do filme.

# Coletando informações
capacidade_assentos = int(input("Informe a capacidade de assentos da sala: "))
valor_ingresso_inteiro = float(input("Informe o valor do Ingresso Inteiro: "))
valor_meio_ingresso = float(input("Informe o valor do Meio Ingresso: "))
num_vendas = int(input("Informe o total de vendas realizadas: "))
num_inteiros = int(input("Informe o número de vendas de Ingresso Inteiro: "))
num_meios = num_vendas - num_inteiros

# Calcular as porcentagens
porcentagem_assentos_vendidos = (num_vendas / capacidade_assentos) * 100
porcentagem_inteiros = (num_inteiros / num_vendas) * 100
porcentagem_meios = (num_meios / num_vendas) * 100

# Calcular totais de vendas
total_venda_inteiros = num_inteiros * valor_ingresso_inteiro
total_venda_meios = num_meios * valor_meio_ingresso
total_receita = total_venda_inteiros + total_venda_meios 

# Imprimir os resultados
print("-"*20)
print(f"Porcentagem de assentos vendidos: {porcentagem_assentos_vendidos:.2f}% ({num_vendas} de um total de {capacidade_assentos})")
print(f"Porcentagem de assentos vendidos como Ingresso Inteiro: {porcentagem_inteiros:.2f}% ({num_inteiros})")
print(f"Porcentagem de assentos vendidos como Meio Ingressos: {porcentagem_meios:.2f}% ({num_meios})")
print("-"*20)
print(f"Total de vendas de Ingresso Inteiros: R${total_venda_inteiros:.2f}")
print(f"Total de vendas de Meio Ingressos: R${total_venda_meios:.2f}")
print(f"Total de receita da sessão: R${total_receita}")
