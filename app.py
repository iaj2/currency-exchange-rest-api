from flask import Flask, jsonify
from flask_cors import CORS
from scraper import currency_exchange_scraper

app = Flask(__name__)
CORS(app)

curr_exchange_rate_dic = currency_exchange_scraper.get_exchange_rates_dic()

# Route to handle GET request for the conversion dictionary
@app.route('/exchange-rates', methods=['GET'])
def get_dictionary():
    return jsonify(curr_exchange_rate_dic)

if __name__ == '__main__':
    app.run()
