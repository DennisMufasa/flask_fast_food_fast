from flask import Flask
from flask import request
from flask import jsonify
import json


app = Flask(__name__)

orders = {}


@app.route('/api/v1/order', methods=['POST'])
def place_order():

    # capturing data from client
    data = request.get_json()

    # converting json to dict
    my_data = json.loads(data)

    # add to data source
    orders.update(my_data)
        
    return jsonify({"Order details" : my_data})


if __name__ == '__main__':
    app.run()
