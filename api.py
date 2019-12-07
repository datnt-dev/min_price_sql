import json
import decimal
from flask import Flask, request, jsonify
from flask_restful import marshal
from database import get_connection
# from flask_marshmallow import Marshmallow


app = Flask(__name__)

def json_encode_decimal(obj):
  if isinstance(obj, decimal.Decimal):
    return str(obj)
  raise TypeError(repr(obj) + " is not JSON serializable")

# endpoint to get min price
# @app.route('/api/minprice/<product_id>', methods=['GET'])
def get_min_price(product_id):
  connect = get_connection()
  cursor = connect.cursor()
  sql = "{CALL GetGiaNhapThapNhat (@tukhoa=?)}"
  params = product_id

  cursor.execute(sql, params)

  rows = cursor.fetchall()
  # data = []
  # column_names = [column[0] for column in cursor.description]
  # for r in row:
  #   data.append(dict(zip(column_names, r)))
  data = []
  for row in rows:
    data.append([x for x in row])
  price_str = json.dumps(data[0][3], default=json_encode_decimal)
  price = float(price_str.replace('"', ''))
  res = {
    'NCC': data[0][4],
    'price': price,
    'thoi_gian_giao_hang': data[0][5]
  }

  return res

@app.route("/api/min/price", methods=['POST', 'GET'])
def get_params():
  data = request.json

  l = []
  for i in data:
    a = get_min_price(i["MA_HANG"])
    l.append(a)
  
  return jsonify(l)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
