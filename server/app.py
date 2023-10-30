from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from models import Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
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


    # Delete a restaurant by ID
@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({"message": "Restaurant deleted successfully"})
    else:
        return jsonify({"error": "Restaurant not found"}), 404


    # Get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(pizza_list)


# Post a new restaurant_pizza
@app.route('/restaurant_pizzas', methods=['POST'])
def post_restaurant_pizza():
    data = request.json
    restaurant_id = data.get("restaurant_id")
    pizza_id = data.get("pizza_id")
    price = data.get("price")

    if restaurant_id is None or pizza_id is None or price is None:
        return jsonify({"error": "Invalid data. Make sure to provide restaurant_id, pizza_id, and price."}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if restaurant is None or pizza is None:
        return jsonify({"error": "Restaurant or Pizza not found"}), 404

    restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=price)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({"message": "RestaurantPizza added successfully"})


if __name__ == '__main__':
    app.run(port=5555, debug=True)

