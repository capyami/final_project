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


def cats_list(list_stars,input_categories, n_tickers):  
    path = './requirements/msedgedriver.exe'
    service = Service(executable_path=path)
    driver = webdriver.Edge(service=service)
    type(driver)
    
    #driver.implicitly_wait(2)
    time.sleep(random.uniform(2.54, 4.1))
    
    url = 'https://es.finance.yahoo.com/screener/etf/new/'
    driver.get(url)
    driver.maximize_window()
    
    time.sleep(random.uniform(1.99, 3.74))
    
    #By.XPATH, "//button[@aria-label='Next']"
    
    # click cookies
    driver.find_element(By.XPATH, "//button[@id='scroll-down-btn']").click()
    
    time.sleep(random.uniform(2.08, 3.71))
    
    # click cookies
    driver.find_element(By.XPATH, "//button[@class='btn secondary reject-all']").click()
    
    time.sleep(random.uniform(1.18, 2.34))
    
    # click for delete filter of NasdaqGM
    driver.find_element(By.XPATH, "//button[@title='Eliminar NasdaqGM']").click()
    
    time.sleep(random.uniform(2.08, 3.1))
    
    # title="★★★★★" stars morningstars
    stars5 = driver.find_element(By.XPATH, "//button[@title='★★★★★']")
    stars4 = driver.find_element(By.XPATH, "//button[@title='★★★★']")
    stars3 = driver.find_element(By.XPATH, "//button[@title='★★★']")
    stars2 = driver.find_element(By.XPATH, "//button[@title='★★']")
    stars1 = driver.find_element(By.XPATH, "//button[@title='★']")
    
    
    for i in range(len(list_stars)):
        if list_stars[i] == '★★★★★':
            stars5.click()
            time.sleep(random.uniform(0.58, 2.1))
        elif list_stars[i] == '★★★★':
            stars4.click()
            time.sleep(random.uniform(0.68, 1.24))
        elif list_stars[i] == '★★★':
            stars3.click()
            time.sleep(random.uniform(0.79, 1.51))
        elif list_stars[i] == '★★':
            stars2.click()
            time.sleep(random.uniform(0.48, 1.98))
        elif list_stars[i] == '★':
            stars1.click()
            time.sleep(random.uniform(1.08, 3.41))
            
    
    #stars5.click()
    #time.sleep(0.5)
    #stars4.click()
    
    time.sleep(random.uniform(1.28, 2.68))
    
    # desplegable categorías
    buttons = driver.find_elements(By.XPATH, '//div[@class="D(ib) Pt(6px) Pb(7px) Pstart(6px) Pend(7px) C($tertiaryColor) Fz(s) Cur(p)"]')
    
    buttons[1].click()
    
    time.sleep(random.uniform(1.78, 2.88))
    
    input_field = driver.find_element(By.XPATH, '//input[@placeholder="Buscar filtros"]')
    
    #input_field.clear()  # Clear 
    
    #category = str(input())
    #category = ['Growth', 'Blend']
    
    time.sleep(random.uniform(1.09, 2.18))
    
    #check_cat = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
    
    #check_cat[12].click()
    
    check_cat1 = driver.find_elements(By.XPATH, '//span[@class="C($tertiaryColor) Mstart(12px) Cur(p) Va(m)"]')
    
    list_cats = []
    for i in range(len(check_cat1)):
        list_cats.append(check_cat1[i].text)
    
    list_cats
    
    #check_cat1[102].click()
    
    # HACER MÁS EFICIENTE EL CÓDIGO, NO ES NECESARIO EL: in list_cats
    for i in range(len(input_categories)):
        if input_categories[i] in list_cats:
            input_field.clear()
            time.sleep(random.uniform(0.68, 2.87))
            input_field.send_keys(input_categories[i])
            time.sleep(random.uniform(1.28, 2.91))
            buttons = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
            time.sleep(random.uniform(1.02, 2.39))
            for i in range(len(buttons)):
                buttons[i].click()
                time.sleep(random.uniform(1.08, 2.5))
    
    #input_search.send_keys(Keys.RETURN)
    time.sleep(random.uniform(1.08, 2.5))
    
    button = driver.find_elements(By.XPATH, '//button[@data-test="find-stock"]')[0]
    button.click()
    
    time.sleep(random.uniform(1.858, 2.79))
    
    buttons = driver.find_elements(By.XPATH, '//th[@class="Ta(end) Pstart(20px) Fz(xs) Py(5px)! Bgc($lv3BgColor) Va(m)  Cur(p) Bgc($hoverBgColor):h  Fw(400)!"]')
    
    # sort tickers by volume
    buttons[3].click()
    time.sleep(random.uniform(2.58, 4.15))
    buttons[3].click()
    time.sleep(random.uniform(1.89, 2.95))
    
    # Find the <a> element
    a_element = driver.find_elements(By.XPATH, '//a[@data-test="quoteLink"]')
    
    len(a_element)
    
    list_etf = []
    for i in range(len(a_element)):
        list_etf.append(a_element[i].text)
    
    if len(list_etf) > int(n_tickers):
        list_etf = list_etf[:int(n_tickers)]
    
    return list_etf
    
    