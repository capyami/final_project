import yfinance as yf
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
def group_list(list_stars, category, n_tickers):
    path = './requirements/msedgedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Edge(service=service)
    
    
    #driver.implicitly_wait(2)
    time.sleep(random.uniform(1.78, 2.53))
    
    url = 'https://es.finance.yahoo.com/screener/etf/new/'
    driver.get(url)
    driver.maximize_window()
    
    time.sleep(random.uniform(2.28, 4.05))
    
    # click cookies
    driver.find_element(By.XPATH, "//button[@id='scroll-down-btn']").click()
    
    time.sleep(random.uniform(1.908, 2.95))
    
    # click cookies
    driver.find_element(By.XPATH, "//button[@class='btn secondary reject-all']").click()
    
    time.sleep(random.uniform(0.82, 2.08))
    
    # click for delete filter of NasdaqGM
    driver.find_element(By.XPATH, "//button[@title='Eliminar NasdaqGM']").click()
    
    time.sleep(random.uniform(0.90, 1.65))
    
    # title="★★★★★" stars morningstars
    stars5 = driver.find_element(By.XPATH, "//button[@title='★★★★★']")
    stars4 = driver.find_element(By.XPATH, "//button[@title='★★★★']")
    stars3 = driver.find_element(By.XPATH, "//button[@title='★★★']")
    stars2 = driver.find_element(By.XPATH, "//button[@title='★★']")
    stars1 = driver.find_element(By.XPATH, "//button[@title='★']")
    
    
    for i in range(len(list_stars)):
        if list_stars[i] == '★★★★★':
            stars5.click()
            time.sleep(random.uniform(0.48, 1.15))
        elif list_stars[i] == '★★★★':
            stars4.click()
            time.sleep(random.uniform(0.41, 1.5))
        elif list_stars[i] == '★★★':
            stars3.click()
            time.sleep(random.uniform(0.68, 1.75))
        elif list_stars[i] == '★★':
            stars2.click()
            time.sleep(random.uniform(1.08, 1.5))
        elif list_stars[i] == '★':
            stars2.click()
            time.sleep(random.uniform(1.08, 2.5))
            
    
    
    time.sleep(1)
    
    buttons = driver.find_elements(By.XPATH, '//div[@class="D(ib) Pt(6px) Pb(7px) Pstart(6px) Pend(7px) C($tertiaryColor) Fz(s) Cur(p)"]')
    
    buttons[1].click()
    
    time.sleep(random.uniform(1.18, 2.35))
    
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Buscar filtros"]')
    
    input_field.clear()  # Clear 
    
    time.sleep(random.uniform(0.91, 2.24))
    
    
    for i in range(len(category)):
    
        if category[i] == 'Value':
            input_field.clear()
            time.sleep(random.uniform(1.18, 3.05))
            input_field.send_keys("Value")
            time.sleep(random.uniform(1.08, 2.5))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(1)
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.21, 2.75))
        
        elif category[i] == 'Growth':
            input_field.clear()
            time.sleep(random.uniform(0.91, 2.45))
            input_field.send_keys("Growth")
            time.sleep(random.uniform(1.28, 2.9))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.18, 2.2))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.1))
        
        elif category[i] == 'Blend':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.5))
            input_field.send_keys("Blend")
            time.sleep(1)
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(1)
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(1)
        
        elif category[i] == 'Financial':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.5))
            input_field.send_keys("Financial")
            time.sleep(random.uniform(1.08, 2.5))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 2.5))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.5))
        
        elif category[i] == 'Technology':
            input_field.clear()
            time.sleep(random.uniform(0.8, 2.5))
            input_field.send_keys("Technology")
            time.sleep(random.uniform(1.08, 1.71))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 2.25))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.38, 2.85))
        
        elif category[i] == 'Commodities':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Commodities")
            time.sleep(random.random(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(1)
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.18, 2.82))
        
        elif category[i] == 'Bonds':
            input_field.clear()
            time.sleep(random.uniform(0.48, 2.52))
            input_field.send_keys("Bond")
            time.sleep(random.random(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.28, 2.82))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(0.68, 3.12))
            input_field.clear()
            time.sleep(random.uniform(0.38, 1.52))
            input_field.send_keys("Government")
            time.sleep(random.random(1.28, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 3.52))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.random(1.08, 4.02))
        
        elif category[i] == 'Large':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Large")
            time.sleep(random.uniform(1.18, 3.32))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.28, 3.02))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.random(1.08, 3.12))
        
        elif category[i] == 'Mid':
            input_field.clear()
            time.sleep(random.random(1.58, 4.12))
            input_field.send_keys("Mid")
            time.sleep(random.uniform(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 2.52))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 3.72))
        
        elif category[i] == 'Small':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.62))
            input_field.send_keys("Small")
            time.sleep(random.uniform(1.18, 2.69))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.random(1.38, 3.52))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(0.08, 3.12))
        
        elif category[i] == 'Health':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.72))
            input_field.send_keys("Health")
            time.sleep(random.random(0.78, 3.04))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.18, 4.52))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.68, 3.12))
            
        elif category[i] == 'Real Estate':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Real Estate")
            time.sleep(random.random(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(0.98, 2.12))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.28, 3.52))
        
        elif category[i] == 'Emerging':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Emerging")
            time.sleep(random.random(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.16, 2.72))
            buttons[0]
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))
        
        elif category[i] == 'Inflation':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Inflation")
            time.sleep(random.uniform(1.08, 2.52))  
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 2.52))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))
        
        elif category[i] == 'Utilities':
            input_field.clear()
            time.sleep(random.uniform(1.08, 2.52))
            input_field.send_keys("Utilities")
            time.sleep(random.uniform(1.08, 3.12))    
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.08, 2.46))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.34))
        else:
        #if category[i] == 'Global':
            input_field.send_keys("China")
            time.sleep(random.uniform(1.08, 3.15))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))
            input_field.clear()
            input_field.send_keys("Stock")
            time.sleep(random.uniform(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))
            input_field.clear()
            input_field.send_keys("Asia")
            time.sleep(random.uniform(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))
            input_field.clear()
            input_field.send_keys("Foreign")
            time.sleep(random.uniform(1.08, 2.52))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.52))

    
    #input_search.send_keys(Keys.RETURN)
    time.sleep(random.uniform(2.08, 3.52))
    
    button = driver.find_elements(By.XPATH, '//button[@data-test="find-stock"]')[0]
    button.click()
    
    time.sleep(random.uniform(3.68, 5.52))
    
    # volume
    buttons = driver.find_elements(By.XPATH, '//th[@class="Ta(end) Pstart(20px) Fz(xs) Py(5px)! Bgc($lv3BgColor) Va(m)  Cur(p) Bgc($hoverBgColor):h  Fw(400)!"]')
    
    buttons[3].click()
    time.sleep(random.uniform(2.15, 2.61))
    
    buttons[3].click()
    time.sleep(random.uniform(2.08, 2.82))
    
    # Find the <a> element
    a_element = driver.find_elements(By.XPATH, '//a[@data-test="quoteLink"]')
    
    len(a_element)
    
    # extract the text from the <a> element
    '''text = a_element[0].text
    text'''
    
    list_etf = []
    for i in range(len(a_element)):
        list_etf.append(a_element[i].text)
    
    if len(list_etf) > int(n_tickers):
        list_etf = list_etf[:int(n_tickers)]
    
    return list_etf