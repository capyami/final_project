def predefined_list(invested_amount):
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
    return list_etf