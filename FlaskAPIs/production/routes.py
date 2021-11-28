from flask import Blueprint, jsonify
from db_fetcher import production_data

production_bp = Blueprint('production_api', __name__,  url_prefix='/production')


@production_bp.route('/brands')
def get_brands():
    return jsonify(production_data.get_brands())