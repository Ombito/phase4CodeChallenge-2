from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

from models import Restaurant, Pizza, RestaurantPizza, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

    # Get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
    return jsonify(restaurant_list)


# Get a specific restaurant by ID
@app.route('/restaurant/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        return jsonify(restaurant_data)
    else:
        return jsonify({"error": "Restaurant not found"}), 404

    #Delete /restaurants/:id
#@app.route('/restaurant/<int:restaurant_id>', methods=['DELETE'])


    # Get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [{"id": pizza.id, "price": pizza.price} for pizza in pizzas]
    return jsonify(pizza_list)

    # Post restaurant_pizzas
#@app.route('/restaurant_pizzas', methods=['POST'])


if __name__ == '__main__':
    app.run(port=5555)
    app.run(debug=True)