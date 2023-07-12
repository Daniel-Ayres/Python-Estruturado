valor_und = 10.00

qntd_comprada = int(input("Informe quantos itens você comprou: "))

valor_total = valor_und * qntd_comprada

if qntd_comprada <= 10:
    print("Seu valor total de compra é:", valor_total)
    print("Infelizmente não há descontos")
elif qntd_comprada <= 20:
    valor_desconto = valor_total * 0.1  # 10% de desconto
    valor_total = valor_total - valor_desconto
    print("Seu valor total de compra é:", valor_total)
    print("Você recebeu um desconto de 10%!")
else:
    valor_desconto = valor_total * 0.2  # 20% de desconto
    valor_total = valor_total - valor_desconto
    print("Seu valor total de compra é:", valor_total)
    print("Você recebeu um desconto de 20%!")
