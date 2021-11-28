from flask import Flask
from flask_restful import Api
from sales.sales_resources import Stores, Store

app = Flask(__name__)
api = Api(app)

api.add_resource(Stores, '/stores', endpoint='Stores')
api.add_resource(Store, '/store', '/store/<int:store_id>', endpoint='Store')

if __name__ == '__main__':
    app.run(debug=True)