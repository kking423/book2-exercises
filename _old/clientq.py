# ex3.8a.py Download stock quotes in CSV


import requests
import time

stock_list = ['GOOG', 'YHOO', 'AOL']

base_url = 'http://download.finance.yahoo.com/d/quotes.csv'

# obtain quote once every 3 seconds for the next 6 seconds
for _ in range(1):

    # retrieve data from web server
    for stock in stock_list:
        data = requests.get(base_url,
                params={'s': stock, 'f': 'sl1d1t1c1ohgv', 'e': '.csv'})

        # write the data to csv
        with open("stocks.csv", "a") as code:
            code.write(data.content)

    # pause for 3 seconds
    time.sleep(3)   
