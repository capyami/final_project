from modules import predefined as pf
from modules import group
from modules import categories as cats
from modules import info
from modules import ratings as rt
from modules import forecast
import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)

# st.session_state
st.set_page_config(layout="wide")
st.title('Forecast of ETFs')
st.markdown('This app is a...')
#st.sidebar.button('click')
col30, col1, col2, col3, col10 = st.columns([1, 3, 3, 3, 1])
invested_amount = col1.number_input('Insert initial amount', 1, 1000000)
years_maintained = col2.slider('Years of maintenance', 1, 25)
type_investment = col3.selectbox(
    'Select type of investment',
    (' ', 'Passive', 'Group', 'Cats'))


if type_investment == 'Group':
    
    col30, col4, col5, col6, col40 = st.columns([1, 3, 3, 3, 1])
    
    category = col4.multiselect(
        'Select group of categories',
        ['Value', 'Growth', 'Blend', 'Financial', 'Technology', 'Commodities', 'Bonds', 'Large', 'Mid', 'Small', 'Health', 'Real Estate', 'Emerging', 'Inflation', 'Utilities', 'Global'])
    
    #st.write('You selected:', options)
    
    list_stars = col5.multiselect(
        'Stars of rating morningstar: ',
        [' ','★★★★★', '★★★★','★★★', '★★', '★'])
    
    n_tickers = col6.number_input('Insert nº of ETFs (1 to 10): ', 1, 10)

if type_investment == 'Cats':
    
    col30, col4, col5, col6, col40 = st.columns([1, 3, 3, 3, 1])
    
    input_categories = col4.multiselect(
        'Select list of categories',
        ['Bank Loan', 'China Region', 'Commodities Broad Basket', 'Convertibles', 'Corporate Bond', 'Diversified Emerging Mkts', 'Diversified Pacific/Asia', 'Emerging Markets Bond', 'Emerging-Markets Local-Currency Bond', 'Energy Limited Partnership', 'Equity Energy', 'Equity Precious Metals', 'Europe Stock', 'Financial', 'Foreign Large Blend', 'Foreign Large Growth', 'Foreign Large Value', 'Foreign Small/Mid Blend', 'Foreign Small/Mid Growth', 'Foreign Small/Mid Value', 'Global Real Estate, Health', 'High Yield Bond', 'High Yield Muni', 'Inflation-Protected Bond', 'Infrastructure', 'Intermediate Government', 'Intermediate-Term Bond', 'Japan Stock', 'Large Blend', 'Large Growth', 'Large Value', 'Long Government', 'Long-Short Credit', 'Long-Short Equity', 'Long-Term Bond', 'Managed Futures', 'Market Neutral', 'Mid-Cap Blend', 'Mid-Cap Growth', 'Mid-Cap Value', 'Miscellaneous Region', 'Multisector Bond', 'Muni California Intermediate', 'Muni California Long', 'Muni Minnesota', 'Muni National Interm', 'Muni National Long', 'Muni National Short', 'Muni New York Intermediate', 'Muni New York Long', 'Muni Single State Long', 'Muni Single State Short', 'Natural Resources', 'Nontraditional Bond', 'Other', 'Pacific/Asia ex-Japan Stk', 'Preferred Stock', 'Real Estate', 'Short Government', 'Short-Term Bond', 'Small Blend', 'Small Growth', 'Small Value', 'Tactical Allocation', 'Technology', 'Trading - Leveraged/Inverse Commodities', 'Trading - Leveraged/Inverse Equity', 'Trading--Inverse Equity', 'Trading--Leveraged Equity,' 'Ultrashort Bond', 'Utilities'])
    

    
    list_stars = col5.multiselect(
        'Stars of rating morningstar: ',
        ['★★★★★', '★★★★','★★★', '★★', '★'])
    
    
    n_tickers = col6.number_input('Insert nº of ETFs (1 to 10): ', 1, 10)    

# button for continue after select
if type_investment != ' ':
    if st.button('Search'):

        if type_investment == 'Passive':
            list_etf = pf.predefined_list(invested_amount)
        elif type_investment == 'Group':
            list_etf = group.group_list(list_stars, category, n_tickers)
        else:
            list_etf = cats.cats_list(list_stars, input_categories, n_tickers)


        basic_info, technic_info, asset_info, top_stocks = info.info_etf(list_etf)
        valuation_ratings, technic_ratings, etf_description = rt.ratings_etf(list_etf)

        st.markdown('Basic info')

        basic_info
        asset_info
        top_stocks
        valuation_ratings
        technic_ratings
        etf_description
        technic_info
        
    
        
        df_final_full_std_by_year, df_final_return_by_active_T, invested_amount_money_of_each_ticker, df_final_full_std_by_year_for_plot = forecast.forecast_etf(list_etf, invested_amount, type_investment, years_maintained)
        df_final_full_std_by_year
        df_final_return_by_active_T
        invested_amount_money_of_each_ticker
        df_final_full_std_by_year_for_plot
        
st.header('DISCLAIMER')