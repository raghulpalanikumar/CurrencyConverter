from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "cdaf602d88342b0fada29a9e"  # ✅ Your working key
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.json['from']
    to_currency = request.json['to']
    amount = float(request.json['amount'])

    url = BASE_URL + from_currency
    res = requests.get(url).json()

    if res['result'] == "success":
        rate = res['conversion_rates'][to_currency]
        converted = round(amount * rate, 2)
        return jsonify({"converted": converted})
    else:
        return jsonify({"error": "API failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
