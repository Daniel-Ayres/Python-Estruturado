def calcular_fatorial(numero):
    """
    Função que calcula o fatorial de um número.
    Recebe um número como parâmetro e retorna o fatorial desse número.
    """
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Informe um número: "))
resultado = calcular_fatorial(numero)

print("O fatorial de", numero, "é:", resultado)
