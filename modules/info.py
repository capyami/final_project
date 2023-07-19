import yfinance as yf
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import random
pd.set_option('display.max_colwidth', None)


def info_etf(list_etf):

    path = './requirements/msedgedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Edge(service=service)
    type(driver)
    
    #driver.implicitly_wait(2)
    secs1 = random.uniform(1.08, 2.1)
    secs2 = random.uniform(2.09, 3.3)
    secs3 = random.uniform(3.15, 4.7)
    secs4 = random.uniform(4.1, 5.15)
    secs5 = random.uniform(4.8, 6.21)
    secs6 = random.uniform(6.4, 7.77)
    secs7 = random.uniform(6.9, 7.8)
    secs8 = random.uniform(7.8, 8.5)
    secs9 = random.uniform(9.1, 10.5)
    secs10 = random.uniform(10.2, 11.5)
    
    
    time.sleep(secs1)
    
    url = 'https://finance.yahoo.com/'
    driver.get(url)
    driver.maximize_window()
    
    time.sleep(random.uniform(1.98, 2.59))
    
    driver.find_element(By.XPATH, "//button[@id='scroll-down-btn']").click()
    
    # click cookies
    driver.find_element(By.XPATH, "//button[@class='btn secondary reject-all']").click()
    
    time.sleep(random.uniform(2.08, 3.1))
    
    basic_info = pd.DataFrame(columns=['Name','Category','expense_ratio','inception_date', 'summary'])
    
    technic_info = pd.DataFrame(columns=['P/E','PER', 'alpha','beta','Mean_Annual_Return','Standard_Deviation','R-Squared','Sharpe_Ratio','Treynor_Ratio'])
    
    asset_info = pd.DataFrame(columns=['Stocks','Sector_Stocks','Bonds', 'Class_Bonds'])
    
    top_stocks = pd.DataFrame(columns=['1', '2', '3', '4', '5', '6', '7', '8', '9','10'])
        
    
    for i in range(len(list_etf)):
        
        ticker = list_etf[i]
    
        driver.find_element(By.XPATH, '//input[@aria-label="Search for news, symbols or companies"]').click()
        
        time.sleep(random.uniform(3.18, 4.3))
        
        input_search = driver.find_element(By.XPATH, '//input[@aria-label="Search for news, symbols or companies"]')
        input_search.send_keys(ticker)
        time.sleep(random.uniform(3.08, 5.1))
        
        try:
            driver.find_element(By.XPATH, '//li[@data-id="result-quotes-0"]').click()
        except NoSuchElementException:
            input_search.clear()
            time.sleep(random.uniform(1.08, 1.81))
            letters_ticker = list(ticker)
            for i in range(len(letters_ticker)):
                input_search.send_keys(letters_ticker[i])
                time.sleep(random.uniform(1.18, 2.31))
            driver.find_element(By.XPATH, '//li[@data-id="result-quotes-0"]').click()

        time.sleep(random.uniform(3.08, 4.1))
        
        # Name of ticker
        name_ticker = driver.find_element(By.XPATH, '//h1[@class="D(ib) Fz(18px)"]').text
        
        PE_ticker = driver.find_element(By.XPATH, '//td[@data-test="PE_RATIO-value"]').text
        
        yield_ticker = driver.find_element(By.XPATH, '//td[@data-test="TD_YIELD-value"]').text
        
        # YTD Daily Total Return
        ytd_ticker = driver.find_element(By.XPATH, '//td[@data-test="YTD_DTR-value"]').text
        
        beta_5y_ticker = driver.find_element(By.XPATH, '//td[@data-test="BETA_5Y-value"]').text
        
        
        expense_ratio_ticker = driver.find_element(By.XPATH, '//td[@data-test="EXPENSE_RATIO-value"]').text
        
        
        fund_inception_date_ticker = driver.find_element(By.XPATH, '//td[@data-test="FUND_INCEPTION_DATE-value"]').text
        
        
        # scroll down
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(random.uniform(2.58, 3.91))
        
        top_holdings_ticker = driver.find_elements(By.XPATH, '//td[@class="Ta(start)"]')
        
        top_holdings_all_ticker = driver.find_elements(By.XPATH, '//tr[@class="Ta(end) BdT Bdc($seperatorColor) H(36px)"]')
        
        list_top_holdings_all_ticker = []
        for i in range(len(top_holdings_all_ticker)):
            top_holdings_stocks_weight = top_holdings_all_ticker[i].text
            #print(top_holdings_stocks_weight)
            top_holdings_stocks_weight = top_holdings_stocks_weight.split(' ')
            #print(top_holdings_stocks_weight)
            if len(top_holdings_stocks_weight) >= 4:
                top_holdings_stocks_weight = [' '.join(top_holdings_stocks_weight[:-2])] + top_holdings_stocks_weight[-2:]
            list_top_holdings_all_ticker.append(top_holdings_stocks_weight)
            
        
        
        # top_holdings_all_ticker7 = top_holdings_all_ticker[7].text
        
        # top_holdings_all_ticker7 = top_holdings_all_ticker7.split(' ')
        
        # if len(top_holdings_all_ticker7) >= 4:
        #     top_holdings_all_ticker7 = [' '.join(top_holdings_all_ticker7[:-2])] + top_holdings_all_ticker7[-2:]
        
        # top_holdings_all_ticker7
        
        
        
        top_holdings_percentage_ticker = driver.find_elements(By.XPATH, '//td[@class=""]')
        try:
            summary_ticker = driver.find_element(By.XPATH, '//div[@class="Lh(21px)"]').text
        except NoSuchElementException:
            summary_ticker = ' '
        
        time.sleep(random.uniform(1.08, 2.1))
        
        # scroll up
        driver.execute_script("window.scrollBy(0,-500)","")
        time.sleep(random.uniform(1.18, 2.31))
        
        # change of tab, holdings
        tabs = driver.find_elements(By.XPATH, '//a[@class="Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b) "]')
        
        tabs[6].click()
        time.sleep(random.uniform(0.85, 1.49))
        
        # overall and weightings equities
        overall_ticker = driver.find_elements(By.XPATH, '//div[@class="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)"]')
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(random.uniform(1.15, 2.47))
        
        holdings_ticker = driver.find_elements(By.XPATH, '//div[@class="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)"]')
        
        
        category_ticker = holdings_ticker[-6].text
        
        
        category_ticker
        
        per_ticker =  holdings_ticker[-21].text
        
        per_ticker = per_ticker.split('\n')
        
        per_ticker = per_ticker[1]
        
        per_ticker
        
        stocks_ticker = holdings_ticker[0].text
        stocks_ticker = stocks_ticker.replace('\n', ' ')
        
        bonds_ticker = holdings_ticker[1].text
        bonds_ticker = bonds_ticker.replace('\n', ' ')
        
        sector_stocks_ticker = []
        for i in range(len(holdings_ticker[2:-21])):
            sector = holdings_ticker[2:-21][i].text
            sector = sector.replace('\n', ' ')
            sector_stocks_ticker.append(sector)
        
        
        class_bonds_ticker = []
        for i in range(len(holdings_ticker[-15:-6])):
            class_bond = holdings_ticker[-15:-6][i].text
            class_bond = class_bond.replace('\n', ' ')
            class_bonds_ticker.append(class_bond)
        
        
        driver.execute_script("window.scrollBy(0,-500)","")
        time.sleep(random.uniform(1.92, 3.21))
        
        tabs = driver.find_elements(By.XPATH, '//a[@class="Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b) "]')
        
        # change of tab
        if len(tabs) == 9:
            tabs[8].click()
            time.sleep(random.uniform(2.58, 4.15))
        else:
            time.sleep(random.uniform(1.18, 2.32))
        
            # change of tab, holdings
            tabs = driver.find_elements(By.XPATH, '//a[@class="Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b) "]')
        
            tabs[5].click()
            time.sleep(random.uniform(1.34, 2.95))
        
            # overall and weightings equities
            overall_ticker = driver.find_elements(By.XPATH, '//div[@class="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)"]')
        
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(random.uniform(1.08, 2.1))
        
            holdings_ticker = driver.find_elements(By.XPATH, '//div[@class="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)"]')
        
        
            category_ticker = holdings_ticker[-6].text
        
        
            category_ticker
        
            per_ticker =  holdings_ticker[-21].text
        
            per_ticker = per_ticker.split('\n')
        
            per_ticker = per_ticker[1]
        
            per_ticker
        
            stocks_ticker = holdings_ticker[0].text
            stocks_ticker = stocks_ticker.replace('\n', ' ')
        
            bonds_ticker = holdings_ticker[1].text
            bonds_ticker = bonds_ticker.replace('\n', ' ')
        
            sector_stocks_ticker = []
            for i in range(len(holdings_ticker[2:-21])):
                sector = holdings_ticker[2:-21][i].text
                sector = sector.replace('\n', ' ')
                sector_stocks_ticker.append(sector)
        
        
            class_bonds_ticker = []
            for i in range(len(holdings_ticker[-15:-6])):
                class_bond = holdings_ticker[-15:-6][i].text
                class_bond = class_bond.replace('\n', ' ')
                class_bonds_ticker.append(class_bond)
        
        
            driver.execute_script("window.scrollBy(0,-500)","")
            time.sleep(random.uniform(1.08, 3.1))
        
            tabs = driver.find_elements(By.XPATH, '//a[@class="Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b) "]')
        
            tabs[7].click()
            time.sleep(random.uniform(2.32, 4.1))


        risk_ticker = driver.find_elements(By.XPATH, '//span[@class="W(39%) Fl(start)"]')
        
        risk_ticker = driver.find_elements(By.XPATH, '//div[@class="Bdbw(1px) Bdbc($seperatorColor) Bdbs(s) H(25px) Pt(10px)"]')
        
        alpha_ticker = risk_ticker[0].text
        
        beta_ticker = risk_ticker[1].text
        
        mean_annual_return_ticker = risk_ticker[2].text
        
        r_squared_ticker = risk_ticker[3].text
        
        sharpe_ratio_ticker = risk_ticker[5].text
        
        treynor_ratio_ticker = risk_ticker[6].text
        
        std_deviation_ticker = risk_ticker[4].text
        
        std_deviation_ticker = std_deviation_ticker.split('\n')
        std_deviation_ticker = std_deviation_ticker[1]
        
        alpha_ticker = alpha_ticker.split('\n')
        alpha_ticker = alpha_ticker[1]
        
        beta_ticker = beta_ticker.split('\n')
        beta_ticker = beta_ticker[1]
        
        mean_annual_return_ticker = mean_annual_return_ticker.split('\n')
        mean_annual_return_ticker = mean_annual_return_ticker[1]
        
        r_squared_ticker = r_squared_ticker.split('\n')
        r_squared_ticker = r_squared_ticker[1]
        
        sharpe_ratio_ticker = sharpe_ratio_ticker.split('\n')
        sharpe_ratio_ticker = sharpe_ratio_ticker[1]
        
        treynor_ratio_ticker = treynor_ratio_ticker.split('\n')
        treynor_ratio_ticker = treynor_ratio_ticker[1]
        
        
        

        
        
        basic_info.loc[ticker] = name_ticker,category_ticker,expense_ratio_ticker, fund_inception_date_ticker, summary_ticker
        technic_info.loc[ticker] = PE_ticker,per_ticker,alpha_ticker, alpha_ticker, mean_annual_return_ticker, std_deviation_ticker, r_squared_ticker, sharpe_ratio_ticker, treynor_ratio_ticker
        asset_info.loc[ticker] = stocks_ticker, sector_stocks_ticker, bonds_ticker, class_bonds_ticker
        list_for_list_top_holdings_all_ticker = []
        if len(list_top_holdings_all_ticker) >= 10:
            for i in range(len(list_top_holdings_all_ticker)):
                list_for_list_top_holdings_all_ticker.append(list_top_holdings_all_ticker[i])
            top_stocks.loc[ticker] = list_for_list_top_holdings_all_ticker
        else:
            top_stocks.loc[ticker] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']
        
    return basic_info, technic_info, asset_info, top_stocks