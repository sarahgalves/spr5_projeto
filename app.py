import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

car_data = pd.read_csv('./vehicles.csv') # lendo os dados

st.header('testee')

st.write('Ainda não é um aplicativo funcional. Em construção.')

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros.\n" \
    "O gráfico com os 5% tinha uma aparência 'achatada', com uma grande concentração somente de um lado")
    
    limite = car_data['price'].quantile(0.95)
    filtered_data = car_data[car_data['price'] <= limite]
     # criar um histograma-------------------o price é coluna dentro da tabela
    fig_plotly = px.histogram(filtered_data, x='price', nbins=50, 
                              title='Distribuição de Preços (sem top 5%)')
    #organiza layout
    fig_plotly.update_layout(xaxis_title='Preço', yaxis_title='Frequência')

    st.plotly_chart(fig_plotly, use_container_width=True)
    