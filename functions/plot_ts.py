import yfinance as yf
import plotly.express as px

def plot(ticker:str):

    data = yf.download('AAPL', period='max', multi_level_index = False)

    df = data.reset_index()[['Date', 'Close']]

    fig = px.line(df, x= 'Date', y = 'Close', titlte = f'Histotico de {ticker}')

    return fig