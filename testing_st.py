from modules import predefined as pf
from modules import group
from modules import categories as cats
from modules import info
from modules import ratings as rt
from modules import forecast
import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)
import plotly.graph_objects as go
import plotly.express as px

# st.session_state
st.set_page_config(layout="wide")
col01, col02, col03, col04, col05 = st.columns([1, 0.1, 5, 0.8, 0.6])
col03.title('Forecast of ETFs')
# col03.markdown('---')
col01.image('./images/chart_lines.png')
col03.markdown('This app for forecast ETFs with big volume and selection by categories')
col04.image('./images/circle_line.png')
#st.sidebar.button('click')
st.markdown('---')
col30, col1, col2, col3, col10 = st.columns([1, 3, 3, 3, 1])
invested_amount = col2.number_input('Insert initial amount', 1, 1000000)
# years_maintained = col2.slider('Years of maintenance', 1, 25)
years_maintained = 25
type_investment = col1.selectbox(
    'Select type of investment',
    (' ', 'Passive', 'Group', 'Categories'))

# col30.markdown('---')
# col30.markdown('---')

# col10.markdown('---')


# col30.image('bull.jpg')

if type_investment == 'Group':
    
    #col30, col1, col2, col3, col10 = st.columns([1, 3, 3, 3, 1])
    
    category = col1.multiselect(
        'Select group of categories',
        ['Value', 'Growth', 'Blend', 'Financial', 'Technology', 'Commodities', 'Bonds', 'Large', 'Mid', 'Small', 'Health', 'Real Estate', 'Emerging', 'Inflation', 'Utilities', 'Global'])
    
    #st.write('You selected:', options)
    
    list_stars = col2.multiselect(
        'Stars of rating MORNINGSTAR: ',
        [' ','★★★★★', '★★★★','★★★', '★★', '★'])
    
    n_tickers = col1.number_input('Insert nº of ETFs (1 to 10): ', 1, 10)

if type_investment == 'Categories':
    
    #col30, col4, col5, col6, col40 = st.columns([1, 3, 3, 3, 1])
    
    input_categories = col1.multiselect(
        'Select list of categories',
        ['Bank Loan', 'China Region', 'Commodities Broad Basket', 'Convertibles', 'Corporate Bond', 'Diversified Emerging Mkts', 'Diversified Pacific/Asia', 'Emerging Markets Bond', 'Emerging-Markets Local-Currency Bond', 'Energy Limited Partnership', 'Equity Energy', 'Equity Precious Metals', 'Europe Stock', 'Financial', 'Foreign Large Blend', 'Foreign Large Growth', 'Foreign Large Value', 'Foreign Small/Mid Blend', 'Foreign Small/Mid Growth', 'Foreign Small/Mid Value', 'Global Real Estate, Health', 'High Yield Bond', 'High Yield Muni', 'Inflation-Protected Bond', 'Infrastructure', 'Intermediate Government', 'Intermediate-Term Bond', 'Japan Stock', 'Large Blend', 'Large Growth', 'Large Value', 'Long Government', 'Long-Short Credit', 'Long-Short Equity', 'Long-Term Bond', 'Managed Futures', 'Market Neutral', 'Mid-Cap Blend', 'Mid-Cap Growth', 'Mid-Cap Value', 'Miscellaneous Region', 'Multisector Bond', 'Muni California Intermediate', 'Muni California Long', 'Muni Minnesota', 'Muni National Interm', 'Muni National Long', 'Muni National Short', 'Muni New York Intermediate', 'Muni New York Long', 'Muni Single State Long', 'Muni Single State Short', 'Natural Resources', 'Nontraditional Bond', 'Other', 'Pacific/Asia ex-Japan Stk', 'Preferred Stock', 'Real Estate', 'Short Government', 'Short-Term Bond', 'Small Blend', 'Small Growth', 'Small Value', 'Tactical Allocation', 'Technology', 'Trading - Leveraged/Inverse Commodities', 'Trading - Leveraged/Inverse Equity', 'Trading--Inverse Equity', 'Trading--Leveraged Equity,' 'Ultrashort Bond', 'Utilities'])
    

    
    list_stars = col2.multiselect(
        'Stars of rating MORNINGSTAR: ',
        ['★★★★★', '★★★★','★★★', '★★', '★'])
    
    
    n_tickers = col1.number_input('Insert nº of ETFs (1 to 10): ', 1, 10)    

# button for continue after select
if type_investment != ' ':
    if col1.button('Search'):

        if type_investment == 'Passive':
            list_etf = pf.predefined_list(invested_amount)
        elif type_investment == 'Group':
            list_etf = group.group_list(list_stars, category, n_tickers)
        else:
            list_etf = cats.cats_list(list_stars, input_categories, n_tickers)


        basic_info, technic_info, asset_info, top_stocks = info.info_etf(list_etf)
        valuation_ratings, technic_ratings, etf_description, mean_bhs, grade_analysts = rt.ratings_etf(list_etf)
        df_final_full_std_by_year, df_final_return_by_active_T, invested_amount_money_of_each_ticker, df_final_full_std_by_year_for_plot, df_final_full_std_by_year_percentage_only = forecast.forecast_etf(list_etf, invested_amount, type_investment, years_maintained)
        
        basic_info.columns = [col.replace('_', ' ') for col in basic_info.columns]
        technic_info.columns = [col.replace('_', ' ') for col in technic_info.columns]
        technic_ratings.columns = [col.replace('_', ' ') for col in technic_ratings.columns]
        valuation_ratings.columns = [col.replace('_', ' ') for col in valuation_ratings.columns]
        etf_description.columns = [col.replace('_', ' ') for col in etf_description.columns]


        basic_info1 = basic_info[['Price', 'Name', 'Category', 'expense ratio', 'inception date']]
        basic_info_summary = basic_info[['summary']]
        
        col5, col6 = st.columns([2, 5])
        # col33.markdown('---')
        #for i in range(len(list_etf)):
        #    col33.checkbox(list_etf[i])
        
        with col6:
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Basic info', 'Consensus Ratings', 'Other ratings', 'Technical info', 'Short description', 'Summary'])
            # 1
            tab1.table(basic_info1)
            # asset_info # not include
            # top_stocks # not include
            # 2
            tab2.table(valuation_ratings)
            # 3
            tab3.table(technic_ratings)
            # 4
            tab4.table(technic_info)
            # 5
            tab5.table(etf_description)
            tab6.table(basic_info_summary)
        with col6.expander("Description technical info"):
            st.markdown('P/E ratio: Measures market valuation and growth expectations by comparing stock price to earnings per share.')
            st.markdown('P/E ratio: Market value and growth expectations comparison - stock price to earnings per share.')
            st.markdown('Alpha: Risk-adjusted excess return vs. benchmark. Positive: Outperformance. Negative: Underperformance. Zero: In line with benchmark.')
            st.markdown("Beta: Measures investment's market risk compared to the overall market.")
            st.markdown("Mean Annual Return: Average yearly investment performance, calculated as the total percentage gain or loss divided by the number of years. It provides an indication of the investment's profitability or risk over time.")
            st.markdown("Standard Deviation: A measure of investment's variability or dispersion from its mean annual return, reflecting the level of risk associated with the investment.")
            st.markdown("Sharpe Ratio: A risk-adjusted performance metric that evaluates an investment's return in relation to its volatility or risk. It measures the excess return earned per unit of risk taken, helping investors assess the investment's risk-adjusted return and compare it to other investment opportunities.")
            st.markdown("Treynor Ratio: A risk-adjusted performance measure that evaluates an investment's excess return per unit of systematic risk, represented by its beta. It helps investors assess the investment's performance relative to its market risk exposure, allowing for comparison with other investments.")
            st.markdown("R-squared (Coefficient of Determination): Measures how well the independent variable predicts the dependent variable, with values between 0 and 1. Higher values indicate a better fit.")
            

        labels = mean_bhs.index
        values = mean_bhs[0]
        custom_colors = ['#0DDABA', '#93CDFB', '#F065FD']
        fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, marker=dict(colors=custom_colors))])
        fig_pie.update_layout(title='Mean of Analysts')

        with col5:
            st.markdown('Grade of Analysts')
            st.title(grade_analysts)
        with col5:
            st.markdown('---')
            # st.markdown('Mean of Analysts')
            st.plotly_chart(fig_pie, theme=None, use_container_width=True)


        col20, col21, col22, col23 = st.columns([0.20, 0.30, 1.5, 3,])
        col21.image('./images/pngwingup.png', output_format="png")
        return_percentage = f'+{df_final_full_std_by_year_percentage_only.iloc[-2][-1].round(2)} %'
        col22.title(return_percentage)
        final_return = f'Final Return:  + {df_final_full_std_by_year_for_plot.T["normal"].iloc[-1].round(2)} $'
        col23.title(final_return)


        col11, col12, col13 = st.columns([1, 5, 1.5])
        
        # col11.markdown('arrow')
        # col11.markdown('%')
        col11.markdown('initial amount')
        col11.markdown('Investment term')



        col11.bar_chart(invested_amount_money_of_each_ticker)

        df_final_full_std_by_year_for_plot.columns = [col.replace('_year', '') for col in df_final_full_std_by_year_for_plot.columns]

        fig_ppl = go.Figure()
        for row in df_final_full_std_by_year_for_plot.index:
            fig_ppl.add_trace(go.Scatter(x=df_final_full_std_by_year_for_plot.columns, 
                                         y=df_final_full_std_by_year_for_plot.loc[row],
                                         mode='lines+markers',
                                         name=f'Row {row}'))

        fig_ppl.update_layout(
            title='Annual Forecast',
            xaxis_title='Years',
            yaxis_title='',
        )



        # Here a table in tab
        col12.plotly_chart(fig_ppl, theme=None, use_container_width=True)
        #col12.plotly_chart(df_final_full_std_by_year_for_plot.T)

        normal_row = df_final_full_std_by_year_percentage_only.loc['normal']
        df_final_full_std_by_year_percentage_only.columns = [col.replace('_year_%', '') for col in df_final_full_std_by_year_percentage_only.columns]

        # Create the horizontal bar chart
        fig_std = go.Figure()

        fig_std.add_trace(go.Bar(
            y=df_final_full_std_by_year_percentage_only.columns,
            x=normal_row,
            orientation='h',
        ))

        fig_std.update_layout(
            title='% by year',
            xaxis_title='%',
            yaxis_title='Years',
        )

        col13.plotly_chart(fig_std, theme=None, use_container_width=True)

st.header('DISCLAIMER')
st.markdown('---')
st.markdown("Disclaimer: The information provided here is intended for educational purposes only and should not be construed as financial advice or a recommendation to invest in any specific exchange-traded fund (ETF). This content is part of an educational project and does not constitute a professional financial analysis. Investing in ETFs involves inherent risks, and past performance is not indicative of future results. Before making any investment decisions, it is essential to consult with a qualified financial advisor and carefully consider your financial goals, risk tolerance, and investment horizon. All investments carry the risk of loss, and there is no guarantee that any investment strategy will achieve its objectives. The educational content provided does not constitute an offer or solicitation for the purchase or sale of any securities or investment products. Investors are encouraged to conduct their own research and due diligence before investing in any ETF or financial instrument. The responsibility for investment decisions rests solely with the individual investor.")
