def calcular_soma_pares(lista):
    """
    Função que calcula a soma dos números pares em uma lista.
    Recebe uma lista como parâmetro e retorna a soma dos números pares.
    """
    soma_pares = 0
    for numero in lista:
        if numero % 2 == 0:  # Verifica se o número é par
            soma_pares += numero  # Adiciona o número par à soma_pares
    return soma_pares

numeros = []

# Loop para solicitar ao usuário que insira 10 números e adicioná-los à lista "numeros"
for i in range(10):
    numero = int(input("Informe um número: "))
    numeros.append(numero)

# Chama a função calcular_soma_pares, passando a lista "numeros" como argumento, e armazena o resultado em "resultado"
resultado = calcular_soma_pares(numeros)

print("A soma dos números pares é:", resultado)  # Exibe a mensagem com a soma dos números pares


