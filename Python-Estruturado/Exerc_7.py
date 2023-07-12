def verificar_primo(numero):
    """
    Função que verifica se um número é primo.
    Recebe um número como parâmetro e retorna True se for primo, False caso contrário.
    """
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Informe um número: "))
resultado = verificar_primo(numero)

if resultado:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
