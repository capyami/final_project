import yfinance as yf
import pandas as pd
import datetime
from datetime import date
import streamlit as st
import numpy as np
import statistics

st.title('Investments')
st.markdown('Description')
st.image('https://www.google.com/imgres?imgurl=https%3A%2F%2Fnapkinfinance.com%2Fwp-content%2Fuploads%2F2021%2F04%2Fassetallocation.jpg&tbnid=VZYIGabzAHD6DM&vet=12ahUKEwiOlN_b3___AhURoUwKHbWUBDcQMygVegUIARDxAQ..i&imgrefurl=https%3A%2F%2Fnapkinfinance.com%2Fnapkin%2Fwhat-is-asset-allocation%2F&docid=kOmpIUt48F6D7M&w=790&h=444&q=asset%20allocation&ved=2ahUKEwiOlN_b3___AhURoUwKHbWUBDcQMygVegUIARDxAQ')


col1, col2 = st.columns(2)
initial_amount = col1.number_input('Insert initial amount', 0, 1000000)
years_maintenance = col2.slider('Years of maintenance', 0, 25)



# select a list of investments
if initial_amount < 5000:
    list_etf = ['^GSPC']
elif initial_amount < 10000:
    list_etf = ['^GSPC', 'GC=F']
elif initial_amount < 25000:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX']
elif initial_amount < 50000:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E'] # global indexes
else:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E', 'EMQQ', 'FEM'] # emergents
    

# dates of data of actives
start = "2012-06-30"
today = '07-07-2023'
# today = date.today().strftime("%Y-%m-%d")

# download the data
list_etf_data = []
for i in range(len(list_etf)):
    print(i)
    etf = yf.download(list_etf[i], start, today)
    list_etf_data.append(etf)

# percentage of each investment

dict_initial_amount = {}
count = 0

if initial_amount < 5000: # only sp500
    investment1 = initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1

elif initial_amount < 10000: # Gold and sp
    investment1 = 0.8*initial_amount/list_etf_data[count]['Close'][-1]
    count = count +1
    dict_initial_amount[list_etf[0]] = investment1
    investment2 = 0.2*initial_amount/list_etf_data[count]['Close'][-1]
    dict_initial_amount[list_etf[1]] = investment2
    
elif initial_amount < 25000: # Gold, nq and sp
    investment1 = 0.4*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.2*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[3]] = investment4
    
elif initial_amount < 50000: # Gold, nq and sp
    investment1 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[3]] = investment4
    count = count +1
    
    investment5 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[4]] = investment5
    count = count +1
    
    investment6 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[5]] = investment6
    count = count +1
    
    investment7 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[6]] = investment7
    count = count +1
    
    investment8 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[7]] = investment8
    count = count +1
    
    investment9 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[8]] = investment9
    
else: # Gold, nq and sp
    investment1 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.1*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[3]] = investment4
    count = count +1
    
    investment5 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[4]] = investment5
    count = count +1
    
    investment6 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[5]] = investment6
    count = count +1
    
    investment7 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[6]] = investment7
    count = count +1
    
    investment8 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[7]] = investment8
    count = count +1
    
    investment9 = 0.08*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[8]] = investment9
    count = count +1
    
    investment10 = 0.06*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[9]] = investment10
    count = count +1
    
    investment11 = 0.06*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[10]] = investment11

# Preprocessing the data, create function for add more features
def add_features(df):
    df = df.reset_index()
    df['HL_pct'] = (df['High'] - df['Low']) / df['Low']
    df['pct_change'] = (df['Close'] - df['Open']) / df['Open']
    df['Date'] = pd.to_datetime(df['Date'])
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    df['day_of_week'] = df['Date'].dt.dayofweek

    # Mapping day of week to actual day names
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day_of_week'] = df['day_of_week'].map(lambda x: day_names[x])
    return df

# use the function each active, return a list of df with new features
for i in range(len(list_etf_data)):
    list_etf_data[i] = add_features(list_etf_data[i])


# separate by year the data of each active, return a dict with key the active and values the df of the active by year
list_etf_data_years = {}

for i in range(len(list_etf_data)):
    years = list_etf_data[i]['year'].unique()
    list_values = []
    for j in range(len(years)):
        x = list_etf_data[i][list_etf_data[i]['year']==years[j]]
        list_values.append(x)
        if j == len(years)-1:
            list_etf_data_years[list_etf[i]] = list_values
        
        


# return a dict of mean of standard deviation of each active of all years

list_etf_data_years_std = {}
for i in range(len(list_etf_data_years)):
    list_values = []
    for j in range(len(list_etf_data_years[list_etf[i]])):  # keys
        x = list_etf_data_years[list_etf[i]][j].describe()['pct_change'].loc['std']
        print(x)
        if x == np.float64('Nan'):
            print(x == np.float64('Nan'))
            x = list_etf_data_years[list_etf[i]][j].describe()['pct_change'].iloc[6]
        x = np.mean(x)
        list_values.append(x)
        if j == len(list_etf_data_years[list_etf[i]])-1:
            list_etf_data_years_std[list_etf[i]] = x
        


# return a dict of percentage of each years of each active

pct_by_years = {}
for i in range(len(list_etf_data_years)): # dict
    list_values = []
    for j in range(len(list_etf_data_years[list_etf[i]])):  # keys
            x = float(list_etf_data_years[list_etf[i]][j][-1:]['Close'])/float(list_etf_data_years[list_etf[i]][j][:1]['Close'])
            list_values.append(x)
            if j == len(list_etf_data_years[list_etf[i]])-1:
                pct_by_years[list_etf[i]] = list_values 
            




# return a dict of mean of percentage of each active by year
pct_by_active = {}

for i in range(len(pct_by_years)):
    list_values = []
    for j in range(len(pct_by_years[list_etf[i]])):
        x = pct_by_years[list_etf[i]][j]
        list_values.append(x)
        if j == len(pct_by_years[list_etf[i]])-1:
            pct_by_active[list_etf[i]] = statistics.mean(list_values)
            
            


# values of investment year to year and final investment, NO MONEY!!

dict_investments = {}
dict_all_values_investments = {}
for i in range(len(list_etf)):
    x = list_etf_data[i]['Adj Close'].iloc[-1]
    list_values = []
    for j in range(years_maintenance):
        x = x*pct_by_active[list_etf[i]]
        list_values.append(x)
        dict_investments[list_etf[i]] = x
        if j == years_maintenance-1:
            dict_all_values_investments[list_etf[i]] = list_values



# return of investment, MONEY!!

final_amount ={}

for i in range(len(dict_initial_amount)):
    final_amount[list_etf[i]] = dict_initial_amount[list_etf[i]]*dict_investments[list_etf[i]]

# sum of all actives, in money

final_total = []
for i in range(len(list_etf)):
    final_total.append(final_amount[list_etf[i]])
    
final_total = sum(final_total)


# value of each active, not final investment, no money invest
df_final = pd.DataFrame(dict_all_values_investments)


# create functions for add standard deviation to the data
def standard_plus(price, st):
    x = price*st
    x = price + x
    return x

def standard_minus(price, st):
    x = price*st
    x = price - x
    return x

# string for add with the name of the active to the column
string_std = '_std_u' # % up
string_std_ = '_std_d' # down


for i in range(len(list_etf)):
    df_final[f'{list_etf[i]}{string_std}'] = list_etf_data_years_std[list_etf[i]]



# copy the dataframe for add columns of standard deviation, not money invest
df_final_std = df_final


# add columns of standard deviation
for i in range(len(list_etf)):
    df_final_std[f'{list_etf[i]}{string_std}'] = df_final.apply(lambda x: standard_plus(x[list_etf[i]],
                                                                                    list_etf_data_years_std[list_etf[i]]),
                                                           axis=1)
    df_final_std[f'{list_etf[i]}{string_std_}'] = df_final.apply(lambda x: standard_minus(x[list_etf[i]],
                                                                                      list_etf_data_years_std[list_etf[i]]),
                                                            axis=1)



cols = []

for i in range(len(list_etf)):
    cols.append(df_final_std.columns[i+len(list_etf)])
    cols.append(df_final_std.columns[i])
    cols.append(df_final_std.columns[i+len(list_etf)*2])




df_final_std = df_final[cols]


df_final_std_invest = df_final_std


count = 0
for i in range(len(list_etf)):
    #i = i*3 # 012,345,678
    df_final_std_invest[df_final_std_invest.columns[count]] = df_final_std_invest[df_final_std_invest.columns[count]]*dict_initial_amount[list_etf[i]]
    df_final_std_invest[df_final_std_invest.columns[count+1]] = df_final_std_invest[df_final_std_invest.columns[count+1]]*dict_initial_amount[list_etf[i]]
    df_final_std_invest[df_final_std_invest.columns[count+2]] = df_final_std_invest[df_final_std_invest.columns[count+2]]*dict_initial_amount[list_etf[i]]
    count = count + 3 # columns of value an std


df_final_std_invest_plot = df_final_std_invest[list_etf]


list_final_invest = []

for i in range(len(df_final_std_invest_plot)):
    list_final_invest.append(df_final_std_invest_plot.iloc[i].sum())

final_result_invest_by_year = pd.DataFrame(list_final_invest)


tab1, tab2, tab3, tab4, tab5 = st.tabs(['Result chart', 'Tickers chart', 'Final result', 'Results', 'Tickers name'])
tab1.line_chart(final_result_invest_by_year)
tab2.line_chart(df_final_std_invest_plot)
tab3.table(final_result_invest_by_year)
tab4.table(df_final_std_invest)
tab5.markdown('Tickers')

st.markdown('DISCLAIMER')