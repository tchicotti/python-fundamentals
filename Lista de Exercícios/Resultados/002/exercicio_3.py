# Exercício 3: Receba uma frase e conte quantas vogais ela possui.
# Exemplo: "Seja bem-vindo"
# Entrada: "Seja bem-vindo"
# Saída: A frase 'Seja bem-vindo' possui 5 vogais.

frase = input("Informe uma frase para contarmos quantas vogais ela tem: ")
contador_vogais = 0

# for letra in frase:
#     if letra in "aeiouAEIOU":
#         contador_vogais = contador_vogais + 1
# ou
for letra in frase.lower():
    if letra in "aeiou": # ["a", "i", "e", "o", "u"]
        contador_vogais = contador_vogais + 1
        
print(f"A frase '{frase}' contém {contador_vogais} vogais.")