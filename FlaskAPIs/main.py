from flask import Flask
from production.routes import production_bp
from sales.routes import sales_blueprint

app = Flask(__name__)
app.register_blueprint(production_bp)
app.register_blueprint(sales_blueprint)

if __name__ == '__main__':
    app.run(debug=True)



# SELECT top 2 * FROM production.brands
# SELECT top 2 * FROM production.categories
# SELECT top 2 * FROM production.products
# SELECT top 2 * FROM production.stocks
# SELECT top 2 * FROM sales.customers
# SELECT top 2 * FROM sales.order_items
# SELECT top 2 * FROM sales.orders
# SELECT top 2 * FROM sales.staffs
# SELECT top 2 * FROM sales.stores
