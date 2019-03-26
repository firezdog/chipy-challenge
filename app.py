from flask import Flask, render_template, request
import requests
# string in Flask can be anything -- what should it be?
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  raw_exchange_rates = requests.get('https://api.exchangeratesapi.io/latest')
  exchange_rates = raw_exchange_rates.json()['rates']
  if request.method == 'GET':
    return render_template('index.html', exchange_rates = exchange_rates)
  return convert_currency(request, exchange_rates)

def convert_currency(request, exchange_rates):
  convert_from_value = exchange_rates[request.form['convert_from']]
  convert_to_value = exchange_rates[request.form['convert_to']]
  amount_to_convert = float(request.form['amount_to_change'])
  rate = convert_from_value / convert_to_value
  result = str(rate * amount_to_convert)
  return result

app.run(debug=True)
