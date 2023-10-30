from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.name} is a good restaurant>'


class Pizza(db.Model):
    __tablename__ = 'pizzas'  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Pizza is {self.name} shillings>'


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas' 
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

        # Validate the price 
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    restaurant = db.relationship('Restaurant', backref='pizzas')
    pizza = db.relationship('Pizza', backref='restaurants')

    def __repr__(self):
        return f'<RestaurantPizza is {self.price} shillings>'
