import yfinance as yf
import pandas as pd
import datetime
from datetime import date
import financedatabase as fd
import streamlit as st
import numpy as np
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
import statistics
pd.set_option('display.max_colwidth', None)

# forecast

def forecast_etf(list_etf, invested_amount, type_investment, years_maintained):
    
    # dates of historical data of actives
    start = "2012-06-30"
    today = date.today().strftime("%Y-%m-%d")
        
    dict_invested_amount_by_ticker = {}
    dict_money_to_ticker = {}
    
    if type_investment == 'Passive':
        if invested_amount < 5000:
            list_etf = ['^GSPC']
        elif invested_amount < 10000:
            list_etf = ['^GSPC', 'GC=F']
        elif invested_amount < 25000:
            list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX']
        elif invested_amount < 50000:
            list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E'] # global indexes
        else:
            list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E', 'EMQQ', 'FEM'] # emergents
        
    
        # download the historical data of each active
        list_etf_data = []
        for i in range(len(list_etf)):
            print(i)
            etf = yf.download(list_etf[i], start, today)
            list_etf_data.append(etf)
            
    
        count = 0
        
        # add proportion of money to each ticker of list_etf in dict, its are units of active purchased
        if invested_amount < 5000: # only sp500
            investment1 = invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[0]] = investment1
            dict_money_to_ticker[list_etf[0]] = invested_amount
        
            
        elif invested_amount < 10000: # Gold and sp
            investment1 = 0.8*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            count = count +1
            dict_invested_amount_by_ticker[list_etf[0]] = investment1
            investment2 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[1]] = investment2
            dict_money_to_ticker[list_etf[0]] = invested_amount*0.8
            dict_money_to_ticker[list_etf[1]] = invested_amount*0.2
        
        
        elif invested_amount < 25000: # Gold, nq and sp
            investment1 = 0.4*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[0]] = investment1
            count = count +1
            
            
            investment2 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[1]] = investment2
            count = count +1
            
            investment3 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[2]] = investment3
            count = count +1
            
            investment4 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[3]] = investment4
            dict_money_to_ticker[list_etf[0]] = invested_amount*0.4
            dict_money_to_ticker[list_etf[1]] = invested_amount*0.2
            dict_money_to_ticker[list_etf[2]] = invested_amount*0.2
            dict_money_to_ticker[list_etf[3]] = invested_amount*0.2
            
            
        elif invested_amount < 50000: # Gold, nq and sp
            investment1 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[0]] = investment1
            count = count +1
            
            investment2 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[1]] = investment2
            count = count +1
            
            investment3 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[2]] = investment3
            count = count +1
            
            investment4 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[3]] = investment4
            count = count +1
            
            investment5 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[4]] = investment5
            count = count +1
            
            investment6 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[5]] = investment6
            count = count +1
            
            investment7 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[6]] = investment7
            count = count +1
            
            investment8 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[7]] = investment8
            count = count +1
            
            investment9 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[8]] = investment9
            
            dict_money_to_ticker[list_etf[0]] = invested_amount*0.2
            dict_money_to_ticker[list_etf[1]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[2]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[3]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[4]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[5]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[6]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[7]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[8]] = invested_amount*0.1
        
            
        else: # Gold, nq and sp
            investment1 = 0.2*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[0]] = investment1
            count = count +1
            
            investment2 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[1]] = investment2
            count = count +1
            
            investment3 = 0.1*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[2]] = investment3
            count = count +1
            
            investment4 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[3]] = investment4
            count = count +1
            
            investment5 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[4]] = investment5
            count = count +1
            
            investment6 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[5]] = investment6
            count = count +1
            
            investment7 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[6]] = investment7
            count = count +1
            
            investment8 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[7]] = investment8
            count = count +1
            
            investment9 = 0.08*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[8]] = investment9
            count = count +1
            
            investment10 = 0.06*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[9]] = investment10
            count = count +1
            
            investment11 = 0.06*invested_amount/list_etf_data[count]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[10]] = investment11
            
            dict_money_to_ticker[list_etf[0]] = invested_amount*0.2
            dict_money_to_ticker[list_etf[1]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[2]] = invested_amount*0.1
            dict_money_to_ticker[list_etf[3]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[4]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[5]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[6]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[7]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[8]] = invested_amount*0.08
            dict_money_to_ticker[list_etf[9]] = invested_amount*0.06
            dict_money_to_ticker[list_etf[10]] = invested_amount*0.06
            
            
    
            
    else:
        # download the historical data of each active
        list_etf_data = []
        for i in range(len(list_etf)):
            print(i)
            etf = yf.download(list_etf[i], start, today)
            list_etf_data.append(etf)
        for i in range(len(list_etf)):
            invested_amount_ticker = invested_amount/len(list_etf)
            investment = invested_amount_ticker/list_etf_data[i]['Adj Close'].iloc[-1]
            dict_invested_amount_by_ticker[list_etf[i]] = investment
            dict_money_to_ticker[list_etf[i]] = invested_amount_ticker
    
    
    
    
    
    invested_amount_money_of_each_ticker = pd.DataFrame.from_dict(dict_money_to_ticker, orient='index', columns=['Amount'])
    
    
    
    # Create function for add more features
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
    dict_etf_data_years = {}
    
    for i in range(len(list_etf_data)):
        years = list_etf_data[i]['year'].unique()
        list_values = []
        for j in range(len(years)):
            x = list_etf_data[i][list_etf_data[i]['year']==years[j]]
            list_values.append(x)
            if j == len(years)-1:
                dict_etf_data_years[list_etf[i]] = list_values
    
    
    
    # return a dict of percentage of each years of each active
    
    pct_each_year_by_active = {}
    for i in range(len(dict_etf_data_years)): # dict
        list_values = []
        for j in range(len(dict_etf_data_years[list_etf[i]])):  # keys
                x = float(dict_etf_data_years[list_etf[i]][j][-1:]['Close'])/float(dict_etf_data_years[list_etf[i]][j][:1]['Close'])
                list_values.append(x)
                if j == len(dict_etf_data_years[list_etf[i]])-1:
                    pct_each_year_by_active[list_etf[i]] = list_values 
                
    
    
    
    # return a dict of mean of percentage of each active by year
    pct_mean_active = {}
    
    for i in range(len(pct_each_year_by_active)):
        list_values = []
        for j in range(len(pct_each_year_by_active[list_etf[i]])):
            x = pct_each_year_by_active[list_etf[i]][j]
            list_values.append(x)
            if j == len(pct_each_year_by_active[list_etf[i]])-1:
                pct_mean_active[list_etf[i]] = statistics.mean(list_values)
                
    
    
    
    # values of investment year to year and final investment, NO MONEY!!
    
    dict_final_result_active_value = {}
    dict_futures_values_actives = {}
    for i in range(len(list_etf)):
        x = list_etf_data[i]['Adj Close'].iloc[-1]
        list_values = []
        for j in range(years_maintained):
            x = x*pct_mean_active[list_etf[i]]
            list_values.append(x)
            dict_final_result_active_value[list_etf[i]] = x
            if j == years_maintained-1:
                dict_futures_values_actives[list_etf[i]] = list_values
    
    
    
    
    
    
    final_invested_amount ={}
    
    for i in range(len(dict_invested_amount_by_ticker)):
        final_invested_amount[list_etf[i]] = dict_invested_amount_by_ticker[list_etf[i]]*dict_final_result_active_value[list_etf[i]]
    
    
    
    
    final_full_return = []
    for i in range(len(list_etf)):
        final_full_return.append(final_invested_amount[list_etf[i]])
        
    final_full_return = sum(final_full_return)
    
    
    
    df_final = pd.DataFrame(dict_futures_values_actives)
    
    
    # return a dict of mean of standard deviation of each active of all years
    
    dict_etf_data_mean_std = {}
    for i in range(len(dict_etf_data_years)):
        list_values = []
        for j in range(len(dict_etf_data_years[list_etf[i]])):  # keys
            x = dict_etf_data_years[list_etf[i]][j].describe()['pct_change'].loc['std']
            if x == np.float64('Nan'):
                print(x == np.float64('Nan'))
                x = dict_etf_data_years[list_etf[i]][j].describe()['pct_change'].iloc[6]
            x = np.mean(x)
            list_values.append(x)
            if j == len(dict_etf_data_years[list_etf[i]])-1:
                dict_etf_data_mean_std[list_etf[i]] = x
    
    
    
    # create functions for add standard deviation to the data
    def standard_up(price, st):
        x = price*st
        x = price + x
        return x
    
    def standard_down(price, st):
        x = price*st
        x = price - x
        return x
    
    # string for add with the name of the active to the column
    string_std = '_std'
    string_std_u = '_std_u' # % up
    string_std_d = '_std_d' # down
    
    # add standard deviation
    for i in range(len(list_etf)):
        df_final[f'{list_etf[i]}{string_std}'] = dict_etf_data_mean_std[list_etf[i]]
        
    
    
    
    
    # add the sum of standard deviation by year
    for i in range(len(df_final[f'{list_etf[0]}{string_std}'])):
        for j in range(len(list_etf)):
            df_final[f'{list_etf[j]}{string_std}'][i] = df_final[f'{list_etf[j]}{string_std}'][i]+df_final[f'{list_etf[j]}{string_std}'][i]*i
    
    
    
    # add columns of standard deviation for up and down
    for i in range(len(list_etf)):
        df_final[f'{list_etf[i]}{string_std_u}'] = df_final.apply(lambda x: standard_up(x[list_etf[i]],
                                                                                        x[f'{list_etf[i]}{string_std}']),
                                                               axis=1)
        df_final[f'{list_etf[i]}{string_std_d}'] = df_final.apply(lambda x: standard_down(x[list_etf[i]],
                                                                                          x[f'{list_etf[i]}{string_std}']),
                                                                axis=1)
    
    
    
    
    
    # create a for,ula for sort columns
    cols = []
    
    for i in range(len(list_etf)):
        cols.append(df_final.columns[i])
        cols.append(df_final.columns[i+len(list_etf)])
        cols.append(df_final.columns[(i+len(list_etf))*2])
        cols.append(df_final.columns[((i+len(list_etf))*2)+1])
    
    
    # sort columns by ticker and standard deviation
    df_final = df_final[cols]
    
    
    
    # copy the data frame for return of money of deviation standard up and down
    df_final_return_by_active = df_final
    
    # deviation standard of the money
    count = 0
    for i in range(len(list_etf)):
        #i = i*3 # 012,345,678
        df_final_return_by_active[df_final_return_by_active.columns[count]] = df_final_return_by_active[df_final_return_by_active.columns[count]]*dict_invested_amount_by_ticker[list_etf[i]]
        df_final_return_by_active[df_final_return_by_active.columns[count+2]] = df_final_return_by_active[df_final_return_by_active.columns[count+2]]*dict_invested_amount_by_ticker[list_etf[i]]
        df_final_return_by_active[df_final_return_by_active.columns[count+3]] = df_final_return_by_active[df_final_return_by_active.columns[count+3]]*dict_invested_amount_by_ticker[list_etf[i]]
        count = count + 4 # columns of value an std
    
    
    
    
    # sort the columns in a list
    
    list_etf_std = []
    count = 0
    
    for i in range(len(list_etf)): # 3 is value plus standard deviatiations
        list_etf_std.append(df_final_return_by_active.columns[count+2])
        list_etf_std.append(df_final_return_by_active.columns[count])    
        list_etf_std.append(df_final_return_by_active.columns[count+3])
        count = count + 4
    
    
    
    # sort the columns in the data frame
    df_final_return_by_active = df_final_return_by_active[list_etf_std]
    
    # transpose the dataframe for years as columns
    df_final_return_by_active_T = df_final_return_by_active.T # for plot and df streamlit
    
    
    # sum of all tickers in a dictionary
    final_sum_return_all = {}
    for i in range(years_maintained):
        list_values_u = []
        list_values = []
        list_values_d = []
        count = 0
        for j in range(len(list_etf)):
            list_values_u.append(df_final_return_by_active_T[i][count])
            list_values.append(df_final_return_by_active_T[i][count+1])
            list_values_d.append(df_final_return_by_active_T[i][count+2])
            count = count + 3
            if j == len(list_etf)-1:
                if i+1 <10:
                    final_sum_return_all[f'0{i+1}_year'] = [sum(list_values_u), sum(list_values), sum(list_values_d)]
                else:
                    final_sum_return_all[f'{i+1}_year'] = [sum(list_values_u), sum(list_values), sum(list_values_d)]
    
    
    
    # create the data frame with the final result
    df_final_full_std_by_year = pd.DataFrame(final_sum_return_all)
    
    # create the dict for change the names of the rows
    row_names = {0 : 'std_up',
                 1 : 'normal',
                 2 : 'std_down'}
    
    # change the names rows
    df_final_full_std_by_year = df_final_full_std_by_year.rename(index = row_names)
    
    
    # copy data frmae for plot the result
    df_final_full_std_by_year_for_plot = df_final_full_std_by_year.copy()
    
    '''    
    # create the function for the change percentage by year
    def percentage_diff(df):
        x = return_/initial
        return x
    '''
    # add percentage, according the invested_amount
    
    for i in range(len(df_final_full_std_by_year.columns)):
        df_final_full_std_by_year[f'{df_final_full_std_by_year.columns[i]}_%'] = (df_final_full_std_by_year[df_final_full_std_by_year.columns[i]]/invested_amount-1)*100
    
    # list for sort the columns
    df_final_full_std_by_year.columns
    list_cols = []
    for i in range(years_maintained):
        list_cols.append(df_final_full_std_by_year.columns[i])
        list_cols.append(df_final_full_std_by_year.columns[i+years_maintained])
    
    # sort the columns in the data frame
    df_final_full_std_by_year = df_final_full_std_by_year[list_cols]
    df_final_full_std_by_year_percentage_only = df_final_full_std_by_year.copy()

    df_final_full_std_by_year_percentage_only

    df_final_full_std_by_year_percentage_only = df_final_full_std_by_year_percentage_only.filter(like='%')

    
    return df_final_full_std_by_year, df_final_return_by_active_T, invested_amount_money_of_each_ticker, df_final_full_std_by_year_for_plot, df_final_full_std_by_year_percentage_only
    
    
    
    
    