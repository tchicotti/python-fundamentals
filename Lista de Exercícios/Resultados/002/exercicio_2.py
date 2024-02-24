# Exercício 2: Solicite um número e imprima a tabuada do número informado.
numero = input("Informe o número que você quer saber a tabuada: ")
numero = int(numero)

for multiplicador in range(11):
    resultado = numero * multiplicador
    # 1ª vez - multiplicador = 1
    # 2ª vez - multiplicador = 2
    # 3ª vez - multiplicador = 3
    # ...
    # 10ª vez - multiplicador = 10
    print(f"{numero} x {multiplicador} = {resultado}")