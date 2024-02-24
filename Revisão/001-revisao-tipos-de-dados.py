# Ao descomentar os códigos abaixo, você poderá ir executando-os para verificar sua saída

# inteiros = 5 # 10 15 -2 -5 INT
# flutuantes = 3.4 # 11.01 25.05 FLOAT 
# e_verdadeiro = True # False BOOLEANOS
# texto = "Esse é um texto" # str STRING
# simples = 'Com aspas simples' # str STRING

# nome = "Tafarel"

# print("Oi, seja bem-vindo nome")
# print("Oi, seja bem-vindo " + nome)
# print(f"Oi, seja bem-vindo {nome}")
# print("Oi, seja bem-vindo {}".format(nome))

# calculo = 100 / 33
# print(f"O resultado de 100 / 33 é: {calculo:.2f}")
# print(f"O resultado de 100 / 33 é: {calculo:.4f}")
# print(f"O resultado de 100 / 33 é: {calculo:10.2f}")

# idade = 22

# if idade == 18:
#     print("Você tem 18 anos") # afirmacao é verdadeira
# else:
#     print("Você não têm 18 anos") # afirmacao é falsa


# if idade == 18:
#     print("Você tem 18 anos") # afirmacao é verdadeira
# elif idade > 18:
#     print("Você é maior que 18 anos") # afirmacao é verdadeira somente quando idade for maior que 18
# else:
#     print("Você não têm 18 anos") # afirmacao é falsa

# idade = 18
# sexo = "feminino"

# if idade >= 18 or sexo == "masculino":
#     print("Bem-vindo ao exército")
# else:
#     print("Você ainda não é parte do exército")

#FOR e WHILE
#FOR é utilizado quando sabemos a quantidade de vezes que queremos executá-lo
#WHILE é quando não sabemos a quantidade de vezes que queremos executá-lo
# 4 * 4 = 16 -> 4²
# 2 * 2 = 4  -> 2²
# for numero_linha in range(1,6):
#     # quadrado = numero_linha * numero_linha
#     quadrado = numero_linha ** 2
#     print(f"O quadrado de {numero_linha} é: {quadrado}")
# print("Fim do meu cálculo")

# for _ in range(3):
#     print("Mensagem sendo impressa 3x")

# lista = ["Tafarel", 32, "Analista", "111.111.111-11", "11.111.111-1"]

# nome, idade, _, *documentos = lista

# idade = lista[1]
# nome  = lista[0]
# # _     = lista[2]
# documentos = lista[3:]

# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print("Documentos", documentos)

# contador = 0
# while contador < 5:
#     #contador = contador + 1
#     contador += 1
#     if contador == 3:
#         continue
#     print("Range Continue: ", contador)
    
# contador = 0
# while contador < 5:
#     #contador = contador + 1
#     contador += 1
#     if contador == 3:
#         break
#     print("Range Break: ", contador)

# lista = []
# lista = ["Tafarel", "Dorival", "Lucio"]
# print(lista)
# lista[1] = "Jéssica"
# print(lista)
# for nome in lista:
#     print(f"O nome da vez é {nome}")

# lista = ["banana", "maçã", "laranja"]
# tupla = ("Tafarel", "Dorival", "Lucio")

# print(lista)
# print(tupla)

# lista.append("carambola")
# print(lista)

# lista.remove("maçã")
# print(lista)

#dicionario = {}

# CHAVE : VALOR
# dados_cliente = {
#     "nome" : "Fulano da Silva",
#     "endereco": "Rua dos Baianos, 101"
# }

# print(dados_cliente)
# print(dados_cliente["nome"])
# print(dados_cliente.get("nome"))

# del dados_cliente["endereco"]
# print(dados_cliente)

# dados_cliente["numero_filhos"] = 1
# print(dados_cliente)

# lista[1] = 2
# dados_cliente["numero_filhos"] = 2
# print(dados_cliente)
