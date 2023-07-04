"""Scrapes web source for exchange rate data"""
from bs4 import BeautifulSoup
import requests


URL = "https://www.exchangerates.org.uk/currency/currency-exchange-rates-table.html"
response = requests.get(URL)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

# Get the exchange table data
table = soup.find("table")
rows = table.find_all("tr")

# Get currency symbols from first row in order
first_row_cells = rows[0].find_all("td")

symbol_list =[]
for cell in first_row_cells:
    a = cell.find('a')
    if a:
        symbol_list.append(a.contents[1])

# Store conversions for each country in dictionary

conv_dic = {}

for i, row in enumerate(rows[1:]):
    cells = row.find_all("td")[2:]  # Skip unneeded cells
    currency_name = symbol_list[i]
    conv_dic[currency_name] = {
        # currency_exchange_name : currency_exchange_rate
        symbol_list[j]: cell.contents[0]
        for j, cell in enumerate(cells)
    }
