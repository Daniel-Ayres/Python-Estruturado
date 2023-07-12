import matplotlib.pyplot as plt



x = ["A", "B", "C", "D"]
y = [3, 8, 1, 10]

plt.bar(x, y)
plt.xlabel("Produtos")
plt.ylabel("Vendas")
plt.title("Dados de Vendas de Produtos")
plt.show()