import pandas as pd
import plotly.express as px
import streamlit as st
data_cars = pd.read_csv('vehicles_us.csv')
st.header('Análisis Exploratorio de Datos de Vehículos en Estados Unidos')
show_hist = st.checkbox('Mostrar Histograma')
if show_hist:
    fig = px.histogram(data_cars, x='odometer', nbins=30,
                       title='Distribución de Años de Vehículos')
    st.plotly_chart(fig, use_container_width=True)
show_disp = st.button('Mostrar Grafico de Dispersión')
if show_disp:
    fig = px.scatter(data_cars, x='odometer', y='price', color='condition',
                     title='Precio vs Año de Vehículos por Condición')
    st.plotly_chart(fig, use_container_width=True)
