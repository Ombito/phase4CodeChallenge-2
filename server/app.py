from flask_cors import CORS
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from models import Restaurant, Pizza, RestaurantPizza, db 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

class RestaurantListResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurant_list = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
        return jsonify(restaurant_list)

class RestaurantResource(Resource):
    def get(self, restaurant_id):
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

    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return jsonify({"message": "Restaurant deleted successfully"})
        else:
            return jsonify({"error": "Restaurant not found"}), 404

class PizzaResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizza_list = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
        return jsonify(pizza_list)

class RestaurantPizzaResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('restaurant_id', type=int, help='Restaurant ID')
        parser.add_argument('pizza_id', type=int, help='Pizza ID')
        parser.add_argument('price', type=float, help='Price')
        data = parser.parse_args()
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

api.add_resource(RestaurantListResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:restaurant_id>')
api.add_resource(PizzaResource, '/pizzas')
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
