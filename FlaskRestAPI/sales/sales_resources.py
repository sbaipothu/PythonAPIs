from flask_restful import Resource, reqparse, fields, marshal_with, abort
from db_fetcher import sales_data
from sales import models

resource_fields = {
    'store_id': fields.Integer,
    'store_name': fields.String,
    'phone': fields.Integer,
    'email': fields.String,
    'street': fields.String,
    'city': fields.String,
    'state': fields.String,
    'zip_code': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('store_name', type=str, help='Store name cannot be empty')
parser.add_argument('phone', type=int, help='Phone no cannot be empty')
parser.add_argument('email', type=str, help='Email name cannot be empty')
parser.add_argument('street', type=str, help='Street name cannot be empty')
parser.add_argument('city', type=str, help='City name cannot be empty')
parser.add_argument('state', type=str, help='State name cannot be empty')
parser.add_argument('zip_code', type=int, help='Zip Code name cannot be empty')


class Stores(Resource):
    def get(self):
        return sales_data.get_stores()


class Store(Resource):
    def get(self, store_id):
        return sales_data.get_store(store_id)

    def put(self, store_id):
        if not sales_data.is_store_exists(store_id):
            abort(404, message = f"Store doesn't exists with id:{store_id}")
        return sales_data.update_store(store_id)

    def delete(self, store_id):
        if not sales_data.is_store_exists(store_id):
            abort(404, message= f"Store doesn't exists with id {store_id}")
        return sales_data.delete_store(store_id), 201

    def post(self):
        args = parser.parse_args()
        store = models.Store(args)
        return sales_data.create_store(store), 200