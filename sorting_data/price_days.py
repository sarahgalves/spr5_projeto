import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

car_data = pd.read_csv('./vehicles.csv') # lendo os dados

def days_price(car_data):
    plt.scatter(car_data['days_listed'], car_data['price'], alpha = 0.4)
    plt.xlabel("Dias desde o anúncio")
    plt.ylabel("Preço")
    plt.title("Tempo no anúncio vs Preço")
    plt.show()