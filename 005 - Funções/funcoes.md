# **Funções em Python**

Neste capítulo, exploraremos as funções em Python, uma parte fundamental da programação que permite a modularização do código, facilitando a organização e a reutilização. Abordaremos desde a estrutura básica até tipos específicos de funções, parâmetros e retorno.

## **O que é uma Função?**

Uma função é um bloco de código que realiza uma tarefa específica e pode ser chamado de outros lugares do programa. Elas ajudam na modularização, promovendo a reutilização de código e tornando o programa mais organizado.

## **Estrutura de uma Função**

A estrutura básica de uma função em Python inclui a palavra-chave `def` seguida pelo nome da função, parênteses que podem conter parâmetros, dois pontos, e o bloco de código indentado que forma o corpo da função. 

```python
def saudacao(nome, saudacao = "Olá"):
    """
    Esta função retorna uma saudação personalizada.

    Parâmetros:
    - nome (str): O nome da pessoa.
    - saudacao (str, opcional): A saudação desejada (padrão é "Olá").

    Retorna:
    - str: A mensagem de saudação personalizada.
    """
    return f"{saudacao}, {nome}!"

# Chamada da função
mensagem: str = saudacao("Alice")
print(mensagem)  # Saída: Olá, Alice!
```

##  Tipos de Funções

### 1. Funções Incorporadas (Nativas)

Python possui uma variedade de funções incorporadas que podem ser usadas sem a necessidade de importar módulos adicionais. Exemplos incluem `print()`, `len()`, `type()`, entre outras.

```python
# Exemplo de função incorporada
tamanho: int = len("Python")
print(tamanho)  # Saída: 6
```

### 2. Funções Criadas por Programadores

Os programadores podem criar suas próprias funções personalizadas. Os tipos de dados nos parâmetros e no retorno são opcionais, mas podem ser declarados para proporcionar uma documentação mais clara ou para garantir a consistência em ambientes colaborativos. 

No exemplo abaixo, o tipo de parâmetro e retorno são declarados, proporcionando maior clareza.

```python
# Exemplo de função criada por programador
def quadrado(numero: float) -> float:
    """
    Esta função retorna o quadrado de um número.

    Parâmetros:
    - numero (float): O número a ser elevado ao quadrado.

    Retorna:
    - float: O quadrado do número.
    """
    return numero ** 2

resultado = quadrado(5)
print(resultado)  # Saída: 25.0
```