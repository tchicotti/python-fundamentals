# Exercício 5: Solicite ao usuário para inserir números até que a soma deles seja maior que 100.
somatorio = 0
contador = 0
while somatorio <= 100:
    numero = input(f"Me informe o número que eu devo somar a {somatorio}: ")
    numero = int(numero)
    contador = contador + 1
    somatorio = somatorio + numero
    
print(f"O total que você digitou, chegou a ser {somatorio}.\nVocê informou {contador} vezes o número para as somas.")
# ou
# print(f"O total que você digitou, chegou a ser {somatorio}.")
# print(f"Você informou {contador} vezes o número para as somas.")