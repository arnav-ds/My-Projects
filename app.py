import streamlit as st

st.set_page_config(
    page_icon='chart_with_upwards_trend:',
    page_title="Trading App",
    layout='wide'
)

st.title('Trading Guide app:bar_chart:')

st.header('We provide the greatest platform for you to collect all information prior to investing in stocks')

st.markdown('## We provide the following services')


st.markdown('#### :one: Stock information')
st.write('Through this page, you can see all information about stock.')

st.markdown('#### :two: Stock Prediction')
st.write('You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models')

st.markdown('#### :three: CAPM Return')
st.write('Discover how Capital Asset Pricing Model (CAPM) calculates the expected returns of different stocks based on its risk ')

st.markdown('#### :four: CAPM Beta')
st.write('Calculates Beta and expected returns for individual stocks')

