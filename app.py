import streamlit as st
from functions.plot_ts import plot

st.title('Historico de cotacoes')
st.write('Veja o historico das cotações das empresas.')

ticker = st.sidebar.text_input('Escolha o ticker:', value = 'AAPL')

fig = plot(ticker)
st.plotly_chart(fig)