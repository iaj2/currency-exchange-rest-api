"""Scrapes web source for exchange rate data"""
from bs4 import BeautifulSoup
import requests

DATA_SOURCE_URL = "https://www.exchangerates.org.uk/currency/currency-exchange-rates-table.html"

class CurrencyExchangeScraper:
    """Scrapes source for currency exchange data"""
    def __init__(self):
        self.url = DATA_SOURCE_URL

    def get_exchange_rates_dic(self):
        """
        Scrapes source for currency exchange data and returns a dictionary object 
        of the currency and its exchange rates
        """
        response = requests.get(self.url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        # Get the exchange table data
        table = soup.find("table")
        rows = table.find_all("tr")

        # Get currency symbols from first row in order
        first_row_cells = rows[0].find_all("td")

        symbol_list = []
        for cell in first_row_cells:
            anchor = cell.find('a')
            if anchor:
                symbol_list.append(anchor.contents[1])

        # Store conversions for each country in dictionary
        conv_dic = {}

        for i, row in enumerate(rows[1:]):
            cells = row.find_all("td")[2:]  # Skip unneeded cells
            currency_name = symbol_list[i]
            conv_dic[currency_name] = {
                # currency_exchange_name: currency_exchange_rate
                symbol_list[j]: cell.contents[0]
                for j, cell in enumerate(cells)
            }

        return conv_dic
