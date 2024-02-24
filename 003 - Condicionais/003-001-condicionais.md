# **Utilização de Condicionais em Python**

Neste capítulo, exploraremos o poder das estruturas condicionais em Python. As condicionais são fundamentais para controlar o fluxo de um programa, permitindo que diferentes blocos de código sejam executados com base em condições específicas. Vamos abordar os seguintes tópicos:

1. **Estrutura Básica de uma Condicional:**
   - Aprenda a estrutura fundamental de uma condicional em Python, utilizando as palavras-chave `if`, `else`, e `elif`.

   ```python
   idade = 18
   if idade >= 18:
       print("Você é maior de idade.")
   else:
       print("Você é menor de idade.")
   ```

2. **Operadores Lógicos:**
   - Introdução aos operadores lógicos (`and`, `or`, `not`) para criar condições mais complexas.

   ```python
   temperatura = 25
   if temperatura > 30 or temperatura < 10:
       print("O clima está extremo.")
   else:
       print("O clima está moderado.")
   ```

3. **Condicionais Aninhadas:**
   - Exploração de condicionais aninhadas, onde múltiplos blocos condicionais são incorporados.

   ```python
   nota = 75
   if nota >= 90:
       print("Excelente!")
   elif nota >= 70:
       print("Bom trabalho!")
   else:
       print("Você pode melhorar.")
   ```

   - Abaixo está um exemplo de um condicional aninhado com um `if` dentro de outro `if`:

    ```python
    idade = 25
    if idade >= 18:
        print("Você é maior de idade.")
        
        if idade >= 21:
            print("E também pode consumir bebidas alcoólicas nos EUA.")
        else:
            print("Mas não pode consumir bebidas alcoólicas nos EUA.")

    else:
        print("Você é menor de idade.")
    ```

    - Neste exemplo, temos um condicional externo que verifica se a idade é maior ou igual a 18. Se essa condição for verdadeira, o código dentro desse bloco é executado, indicando que a pessoa é maior de idade. 
    - Dentro desse bloco, há outro condicional interno que verifica se a idade é maior ou igual a 21, e imprime mensagens relacionadas ao consumo de bebidas alcoólicas nos EUA com base na idade. Se a condição externa (`idade >= 18`) for falsa, o código dentro do bloco `else` é executado, indicando que a pessoa é menor de idade.

4. **Condicionais com Estruturas de Dados:**
   - Utilização de condicionais com listas, dicionários e outras estruturas de dados.

   ```python
   lista_numeros = [1, 2, 3, 4, 5]
   if 3 in lista_numeros:
       print("O número 3 está na lista.")
   ```

5. **Ternary Operator:**
   - Introdução ao operador ternário para escrever condicionais de forma mais concisa.

   - A estrutura condicional ternária em Python é uma forma concisa de escrever uma instrução `if-else` em uma única linha. Sua sintaxe geral é a seguinte:

    ```python
    valor_se_verdadeiro if condição else valor_se_falso
    ```

    - Essa expressão avalia a condição. Se a condição for verdadeira, o valor antes do `if` é retornado; caso contrário, o valor após o `else` é retornado. A estrutura ternária é útil quando se deseja atribuir um valor com base em uma condição de forma mais compacta.

    - Aqui está um exemplo simples:

    ```python
    idade = 20
    status = "Maior de idade" if idade >= 18 else "Menor de idade"
    print(status)
    ```

    - Neste exemplo, a variável `status` recebe o valor "Maior de idade" se a condição `idade >= 18` for verdadeira, caso contrário, recebe o valor "Menor de idade". A mensagem impressa será "Maior de idade" se a idade for 18 ou mais, e "Menor de idade" caso contrário.
    
    - A estrutura condicional ternária é especialmente útil quando se deseja atribuir valores simples com base em condições, proporcionando uma sintaxe mais enxuta em comparação com a instrução `if-else` tradicional.


## **Conclusão**


Ao final deste capítulo, você estará apto a utilizar condicionais de maneira eficaz, permitindo que seus programas tomem decisões dinâmicas com base nas condições estabelecidas. Prepare-se para aprimorar seu controle de fluxo em Python!