import yfinance as yf
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
import financedatabase as fd
import random

def ratings_etf(list_etf):
    path = './requirements/msedgedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Edge(service=service)
    type(driver)
    
    #driver.implicitly_wait(2)
    time.sleep(random.uniform(2.08, 4.12))
    
    url = 'https://www.tipranks.com/stocks/googl'
    driver.get(url)
    #driver.maximize_window()
    
    time.sleep(random.uniform(21.08, 26.52))
    
    # click cookies
    driver.find_element(By.XPATH, '//button[@title="Scroll to the bottom of the text below to enable this button"]').click()
    time.sleep(random.uniform(4.28, 6.52))
    
    valuation_ratings = pd.DataFrame(columns=['Grade','Consensus', 'Buy', 'Hold', 'Sell', 'Highest_target','Average_target','Lowest_target'])
        
    technic_ratings = pd.DataFrame(columns=['Blogger_sentiment','Hedge_Fund_Trend','Crowd_Wisdom','News_Sentiment','SMA','Momentum'])
        
    etf_description = pd.DataFrame(columns=['ETF_description'])
    
    for i in range(len(list_etf)):
        
        # etfs = fd.ETFs()
        # etfs = etfs.search()
        # name_ticker = etfs.filter(like=list_etf[i], axis=0)['name'][0]
        ticker = list_etf[i]
        if '.' in list_etf[i]:
            continue
        #ticker = ticker.split('.')
        #ticker = ticker[0]
        # click for to write
        lens = driver.find_element(By.XPATH, '//button[@class="colorgray-3 displaynone fontSize6 px4 laptop_displayflex"]')
        
        lens.click()
        time.sleep(random.uniform(1.08, 2.52))
        # clilk lens with bar
        search_input = driver.find_element(By.XPATH, '//input[@placeholder="Search ..."]')
        
        search_input.click()
        
        # ticker = 'spy'
        
        search_input.send_keys(ticker)
        # search_input.send_keys(name_ticker+f'({ticker})')

        time.sleep(2)
        
        test_elements = driver.find_elements(By.XPATH, '//a[@class="colorblack-4 fontFamilyregular truncate flexrsb displayflex hoverCursorpointer w12 px4 py3 fontWeightsemibold"]')

        for i in range(len(test_elements)):
            if 'ETF' in test_elements[i].text or 'Trust' in test_elements[i].text or 'Fund' in test_elements[i].text or 'Hedge' in test_elements[i].text or 'Etf' in test_elements[i].text:
                test_elements[i].click()
                break
        # select th first
        
        '''        try:
            first_ticker = driver.find_element(By.XPATH, '//div[@class="flexrsb w5    displayflex"]')
        
            first_ticker.click()
            #time.sleep(5)
        except NoSuchElementException:
            search_input.click()
            time.sleep(2)
            search_input.clear()
            time.sleep(0.5)
            search_input.send_keys(ticker)
            time.sleep(2)
            first_ticker = driver.find_element(By.XPATH, '//div[@class="flexrsb w5    displayflex"]')
            first_ticker.click()'''

        time.sleep(random.uniform(19.8, 24.52))

        
        # click cookies
        driver.find_element(By.XPATH, '//button[@title="Scroll to the bottom of the text below to enable this button"]').click()
        time.sleep(random.uniform(3.78, 5.32))
        try:
            button_outperform = driver.find_element(By.XPATH, '//span[@class="fontSizebig fontWeightbold    h_pxsmall  mb1"]')
            Outperform = button_outperform.text
        except NoSuchElementException:
            variable_test = ' '
            Outperform = ' '
            # button_outperform = ' '

        try:
            button_ratings1 = driver.find_elements(By.XPATH, '//span[@class="colorblack fonth10_semibold"]')
            if len(button_ratings1) != 0:
                Average_Price_Target = button_ratings1[0].text
            else:
                Average_Price_Target = ' '
        except NoSuchElementException:
            variable_test = ' '
            Average_Price_Target = ' '
                # buttons header reatings


        try:
            button_ratings2 = driver.find_elements(By.XPATH, '//div[@class="flexrcc     displayflex"]')
            if len(button_ratings2) == 15:
                Analyst_consensus = button_ratings2[4].text
                Blogger_Sentiment = button_ratings2[5].text
                Hedge_Fund_Trend = button_ratings2[6].text
                Crowd_Wisdom = button_ratings2[7].text
                News_Sentiment = button_ratings2[8].text
                Technical_SMA = button_ratings2[9].text
                Technical_Momentum = button_ratings2[10].text
            
            elif len(button_ratings2) > 12:
                Analyst_consensus = button_ratings2[4].text
                Blogger_Sentiment = button_ratings2[5].text
                Hedge_Fund_Trend = button_ratings2[6].text
                Crowd_Wisdom = button_ratings2[7].text
                News_Sentiment = ' '
                Technical_SMA = button_ratings2[-6].text
                Technical_Momentum = button_ratings2[-5].text
            
            elif len(button_ratings2) < 13 and len(button_ratings2) > 10:
                Analyst_consensus = button_ratings2[4].text
                Blogger_Sentiment = ' '
                Hedge_Fund_Trend = button_ratings2[5].text
                Crowd_Wisdom = ' '
                News_Sentiment = ' '
                Technical_SMA = button_ratings2[6].text
                Technical_Momentum = button_ratings2[7].text
        

            elif len(button_ratings2) < 11 and len(button_ratings2) > 7:
                Analyst_consensus = button_ratings2[4].text
                Blogger_Sentiment = ' '
                Hedge_Fund_Trend = ' '
                Crowd_Wisdom = ' '
                News_Sentiment = ' '
                Technical_SMA = button_ratings2[5].text
                Technical_Momentum = button_ratings2[6].text

            else:
                variable_test = ' '
                Analyst_consensus = ' '
                Blogger_Sentiment = ' '
                Hedge_Fund_Trend = ' '
                Crowd_Wisdom = ' '
                News_Sentiment = ' ' 
                Technical_SMA = ' '
                Technical_Momentum = ' '
        
        except NoSuchElementException:
            variable_test = ' '
            Analyst_consensus = ' '
            Blogger_Sentiment = ' '
            Hedge_Fund_Trend = ' '
            Crowd_Wisdom = ' '
            News_Sentiment = ' ' 
            Technical_SMA = ' '
            Technical_Momentum = ' '


            
        etf_description_text = driver.find_element(By.XPATH, '//div[@class="px4"]')
        etf_description_text = etf_description_text.text
        #<div class="px4">SPY tracks a market cap-weighted index of US large- and mid-cap stocks selected by the S&amp;P Committee.</div>
            
        # change to analysis forecast
        random.uniform(1.08, 2.52)
                
        # change to analysis forecast
        to_forecast = driver.find_elements(By.XPATH, '//a[@data-link="etf-forecast"]')

        if len(to_forecast) > 0:    

            to_forecast[1].text
    
            to_forecast[1].click()
            time.sleep(random.uniform(3.28, 5.27))
    
            buttons_forecast_b = driver.find_elements(By.XPATH, '//span[@class="mr2"]')
    
            ratings_Buy = buttons_forecast_b[0].text
            ratings_Hold =  buttons_forecast_b[1].text
            ratings_Sell = buttons_forecast_b[2].text
    
            price_forecast = driver.find_elements(By.XPATH, '//tr[@class="w12 fontSize5 fontWeightsemibold flexrs_ maxW480 laptop_px0 laptop_fontSize7 laptop_flexrb_"]')
    
            price_consensus = price_forecast[0].text
            price_consensus
    
            list_price_target = price_consensus.split('\n')
    
            Highest_Price_Target = list_price_target[1]
    
            Average_Price_Target = list_price_target[3]
    
            Lowest_Price_Target = list_price_target[5]

        else:       
            ratings_Buy = ' '
            ratings_Hold = ' '
            ratings_Sell = ' '
            price_forecast = ' '
            price_consensus = ' '
            list_price_target =  ' '
            Highest_Price_Target =  ' '
            Average_Price_Target =  ' '
            Lowest_Price_Target =  ' '

        
        valuation_ratings.loc[ticker] = [Outperform, Analyst_consensus, ratings_Buy, ratings_Hold, ratings_Sell, Highest_Price_Target, Average_Price_Target, Lowest_Price_Target]
        
        technic_ratings.loc[ticker] = [Blogger_Sentiment, Hedge_Fund_Trend, Crowd_Wisdom, News_Sentiment, Technical_SMA, Technical_Momentum]
    
        etf_description.loc[ticker] = [etf_description_text]

        valuation_ratings_bhs = valuation_ratings.copy()
        valuation_ratings_bhs = valuation_ratings_bhs[['Buy', 'Hold', 'Sell']]

        valuation_ratings_bhs['Buy'] = valuation_ratings_bhs['Buy'].apply(lambda x: x.replace('%', ''))
        valuation_ratings_bhs['Hold'] = valuation_ratings_bhs['Hold'].apply(lambda x: x.replace('%', ''))
        valuation_ratings_bhs['Sell'] = valuation_ratings_bhs['Sell'].apply(lambda x: x.replace('%', ''))

        valuation_ratings_bhs[['Buy', 'Hold', 'Sell']] = valuation_ratings_bhs[['Buy', 'Hold', 'Sell']].astype(float)

        mean_bhs = valuation_ratings_bhs.mean()
        mean_bhs = pd.DataFrame(mean_bhs)
       
        grade_analysts = valuation_ratings.copy()
        
        sum_outperform = []
        for i in range(len(grade_analysts)):
            sum_outperform.append(float(valuation_ratings.iloc[i][0]))
        grade_analysts = sum(sum_outperform)/len(grade_analysts)
        grade_analysts = round(grade_analysts, 2)
        grade_analysts 

    return valuation_ratings, technic_ratings, etf_description, mean_bhs, grade_analysts
    