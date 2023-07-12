while True:
    try:
        numero = float(input("Digite um número: "))
        print("Número inserido:", numero)
        break  # Sai do loop se um número válido for inserido
    except ValueError:
        print("Número não inserido. Digite apenas um valor numérico.")
