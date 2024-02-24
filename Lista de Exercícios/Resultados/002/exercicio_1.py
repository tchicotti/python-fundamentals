"""
As 7 operações da matemática são:
+  Soma
-  Subtração
*  Multiplicação
/  Divisão
// Divisão truncado (somente a parte inteira)
** Potência
%  Resto da Divisão
"""

# Exercício 1: Solicite um número ao usuário e imprima se ele é par ou ímpar.
numero = input("Informe o número que deseja descobrir se é par ou ímpar: ")
numero = int(numero)

if numero % 2 == 0:
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")

