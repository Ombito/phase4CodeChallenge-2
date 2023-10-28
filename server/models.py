from flask_sqlalchemy import sqlalchemy 

db = sqlalchemy()

    # restaurant table
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas', backref='restaurants')

    def __repr__(self):
        return f'<Restaurant {Restaurant.name} is a good restaurant>'
    
    # pizza table
class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    restaurants = db.relationship('Restaurant', secondary='restaurant_pizzas', backref='pizzas')

    def __repr__(self):
        return f'<Pizza is {Pizza.price} shillings>'

    # restaurant pizza association table
class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', backref='restaurant_pizzas')
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')

    def __repr__(self):
        return f'<RestaurantPizza is {self.price} shillings>'