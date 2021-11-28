from flask import Blueprint, jsonify, request
from db_fetcher import sales_data
from .models import Store

sales_blueprint = Blueprint('sales_api', __name__, url_prefix='/sales')


@sales_blueprint.route('/stores', methods=['GET'])
def get_stores():
    return jsonify(sales_data.get_stores())


@sales_blueprint.route('/store', methods=['GET', 'POST', 'PUT', 'DELETE'])
def store():
    if request.method == 'POST':
        store = Store(request.form)
        if store.validate_store():
            try:
                sales_data.create_store(store)
                return jsonify({"message": "Successfully added the store"}), 200
            except Exception as e:
                return jsonify({"message": f"Couldn't add the store. Details.{str(e)}"}), 500
            return jsonify(sales_data.create_store(store)), 200
        return jsonify({"message": "Coudn't add the store details"}), 400
    else:
        store_id = request.args.get('store_id')
        # https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        if request.method == 'GET':
            return jsonify(sales_data.get_store(store_id))
        elif request.method == 'DELETE':
            return jsonify(sales_data.delete_store(store_id)), 201
        elif request.method == 'PUT':
            return jsonify({"message": "Didn't implement the functionality yet"}), 200
