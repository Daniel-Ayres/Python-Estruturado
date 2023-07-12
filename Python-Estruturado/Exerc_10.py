import numpy as np
import matplotlib.pyplot as plt

# Gerar 1000 pontos seguindo a distribuição normal
media = 20
desvio_padrao = 2
dados = np.random.normal(media, desvio_padrao, 1000)

# Plotar o histograma
plt.hist(dados, bins=30, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()
