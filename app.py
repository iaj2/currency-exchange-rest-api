from flask import Flask, jsonify

app = Flask(__name__)

my_dictionary = {}

# Route to handle GET request for the conversion dictionary
@app.route('/exchange-rates', methods=['GET'])
def get_dictionary():
    return jsonify(my_dictionary)

if __name__ == '__main__':
    app.run()
