import re
from bs4 import BeautifulSoup
import requests


url = "https://www.exchangerates.org.uk/currency/currency-exchange-rates-table.html"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

# Get the exchange table data
table = soup.find("table") 
rows = table.find_all("tr")

# Get currency symbols from first row in order
symbol_pattern = r'([A-Z]{3})'

first_row_cells = rows[0].find_all("td")

symbol_list =[]
for cell in first_row_cells:
    if cell.text:
      symbol_list.append(re.search(symbol_pattern,cell.text).group(0))
