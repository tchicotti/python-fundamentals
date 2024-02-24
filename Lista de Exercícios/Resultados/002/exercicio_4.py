# Exercício 4: Receba o total de vendas realizadas por um vendedor de uma loja e calcule o valor de sua comissão.
# Se o vendedor vendeu até R$ 1.000,00. Ele deve receber uma comissão de 5% do valor da venda.
# Se o vendedor vendeu entre R$ 1.000,00 e R$ 5.000,00. Ele deve receber uma comissão de 7.5% do valor da venda.
# Se o vendedor vendeu acima de R$ 5.000,00. Ele deve receber uma comissão de 9% do valor da venda.

valor_vendas = float(input("Informe o total de vendas realizadas: "))

if valor_vendas < 1000:
    # menor que 1000
    porcentagem = 5 / 100 # 0.05
elif valor_vendas >= 1000 and valor_vendas <= 5000:
    # entre 1000 e 5000
    porcentagem = 7.5/100 # 0.075
else:
    # acima de 5000
    porcentagem = 9 / 100

comissao = valor_vendas * porcentagem
print(f"O total de vendas foi de R${valor_vendas:.2f}")
print(f"A comissão do vendedor foi de R${comissao:.2f}")