import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('TkAgg')  # ou 'Qt5Agg'
#|-> pois o gráfico não estava rodando

import matplotlib.pyplot as plt

car_data = pd.read_csv('c:/Users/sarah/OneDrive/Documents/GitHub/spr5_projeto/vehicles.csv') # lendo os dados

#print(car_data['price'].describe())

'''O gráfico com
car_data['price'].plot(kind = 'hist', bins = 30)
tinha uma aparência 'achatada' com uma grande concentração somente de um lado'''

fig, ax = plt.subplots()
limite = car_data['price'].quantile(0.95)
car_data[car_data['price'] <= limite]['price'].hist(bins=50)
ax.set_title('Distribuição de Preços excluindo os 5% mais caros')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

fig.savefig('price_graph.png')
plt.close(fig)