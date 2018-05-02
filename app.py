from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 25.0
            }
        ]
    }
]

#/
@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'store': new_store})


#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store': store})
    return jsonify({'error': 'store doesn\'t exist'})


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
    'name': request_data['name'],
    'price': request_data['price']
    }

    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify({'new item': new_item})
    return jsonify({'error': 'store doesn\'t exist'})



#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'error': 'store doesn\'t exist'})

app.run(port=5000)
