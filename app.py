import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('./vehicles.csv') # lendo os dados

st.header('Análise de anúncios de vendas de carros')

st.write('Escolha qual gráfico quer ver primeiro:')

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
    fig_plotly.update_layout(xaxis_title='Preço', yaxis_title='Quantidade', template="plotly_white")
    fig_plotly.update_xaxes(showgrid=True)  # linhas verticais
    fig_plotly.update_yaxes(showgrid=True)  # linhas horizontais

    st.plotly_chart(fig_plotly, width="stretch")

scatt_button = st.button('Dias vs Preço')

if scatt_button:
    st.write("Criando um gráfico que correlaciona preço, milhagem e condição do carro.")
    st.write("Atenção! Gráfico interativo. Clique na legenda para escolher se quer alguma condição específiva.")

    car_data['condition'] = car_data['condition'].map({
    "good": "Bom",
    "like new": "Quase Novo",
    "fair": "Justo",
    "excellent": "Excelente",
    "salvage": "Batido",
    "new": "Novo"
    })

    graph = px.scatter(
    car_data,
    x="odometer",
    y="price",
    #color recebe o nome de uma coluna do DataFrame (numérica ou categórica)
    #Plotly automáticamente atribui cores diferentes para cada valor dessa coluna
    color="condition",  # legenda automática
    title="Preço vs Odometro vs Condição",
    labels={
        "odometer": "Odometro (milhas)",
        "price": "Preço ($)",
        "condition": "Condição"
    },
    hover_data=["model", "model_year"],  # info extra ao passar o mouse
    )

    # Ajustes de layout
    graph.update_layout(
        title={
            "x": 0.5,  # centraliza título
            "xanchor": "center"
        },
        legend_title="Condição do carro",
        template="plotly_white"
    )
    graph.update_yaxes(range=[0, None])  # 0 = mínimo, None = deixa o máximo automático

    #graph.show() -->o .show() faz abrir em uma nova aba. por isso:
    st.plotly_chart(graph, width="stretch")