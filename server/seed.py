from app import app, db

with app.app_context():
    from models import Restaurant, Pizza, RestaurantPizza

    # create some restaurants
    restaurant1 = Restaurant(name="Sottocasa NYC", address="298 Atlantic Ave, Brooklyn, NY 11201")
    restaurant2 = Restaurant(name="PizzArte", address="69 W 55th St, New York, NY 10019")
    restaurant3 = Restaurant(name="Pizzeria", address="123 Main Street, Los Angeles, CA 90001")
    restaurant4 = Restaurant(name="Pizza Inn", address="456 Elm Avenue, Chicago, IL 60601")
    restaurant5 = Restaurant(name="Miale", address="789 Maple Lane, San Francisco, CA 94101")
    restaurant6 = Restaurant(name="Pizza Hub", address="101 Pine Street, Miami, FL 33125")

    # create some pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Margherita Pizza", ingredients="Lettuce, Tomato, Cucumber, Red Onion")
    pizza4 = Pizza(name="Hawaiian Pizza", ingredients="Flour, Sugar, Butter, Eggs")
    pizza5 = Pizza(name="Vegetarian Pizza", ingredients="Chicken, Rice, Black Beans, Avocado")
    pizza6 = Pizza(name="BBQ Chicken Pizza", ingredients="Spinach, Feta Cheese, Olives, Olive Oil")

    # create some restaurant pizzas
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=12, restaurant=restaurant5, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=14, restaurant=restaurant4, pizza=pizza3)
    restaurant_pizza4 = RestaurantPizza(price=13, restaurant=restaurant3, pizza=pizza4)
    restaurant_pizza5 = RestaurantPizza(price=10, restaurant=restaurant6, pizza=pizza5)
    restaurant_pizza6 = RestaurantPizza(price=11, restaurant=restaurant2, pizza=pizza6)

    print("Seeding data...")
    # add the instances to the database
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()