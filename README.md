# Flask Code Challenge - Pizza Restaurants


This is a Flask application that manages Pizza Restaurants and their associated Pizzas through the `RestaurantPizza` model. This application is built to interact with a backend API that handles the Pizza Restaurant domain, including models, relationships, and validations.


## Getting Started

To set up and run the project, follow these steps:

1. Install project dependencies for both the backend and frontend:
   
   ```bash
   pipenv install
   npm install 
   ```

2. Create the required database tables and seed data:

   - Generate the models and migrations for the database tables.

   - Run the migrations and seed data with the following commands:

   ```bash
   flask db upgrade
   python app/seed.py
   ```


3. Run the Flask API on `localhost:5555`:

   ```bash
   python app.py
   ```

4. Run the React app on `localhost:4000`:

   ```bash
   npm start 
   ```

The React frontend application should now be running on `http://localhost:3000`.

## Models

The Pizza Restaurant domain includes the following models and relationships:

- `Restaurant` has many `Pizza`s through `RestaurantPizza`.
- `Pizza` has many `Restaurant`s through `RestaurantPizza`.
- `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`.

These models are implemented in the backend API, and this frontend application interacts with them through API requests.

## Validations

The `RestaurantPizza` model in the backend API has the following validation:

- `price` must be between 1 and 30.

## Routes

The Pizza Restaurant React frontend application interacts with the following API routes. Each route corresponds to a specific HTTP verb and returns data in the specified JSON format:

- **GET /restaurants**: Retrieve a list of all restaurants.
- **GET /pizzas**: Retrieve a list of all pizzas.
- **POST /restaurants**: Create a new restaurant.
- **POST /restaurants_pizzas**: Create a new pizza.
- **GET /restaurant-pizzas**: Retrieve a list of all restaurant-pizza relationships.
- **POST /restaurant-pizzas**: Create a new restaurant-pizza relationship.
- **PUT /restaurant-pizzas/:id**: Update an existing restaurant-pizza relationship.
- **DELETE /restaurant-pizzas/:id**: Delete an existing restaurant-pizza relationship.

## Usage

This React frontend application allows you to interact with the Pizza Restaurant domain through a user-friendly interface. You can perform the following actions:

- View a list of all restaurants and their associated pizzas.
- View a list of all pizzas and the restaurants where they are available.
- Create new restaurants and pizzas.
- Create new relationships between restaurants and pizzas.
- Delete restaurants by id.

Please refer to the application's user interface for a seamless experience.

## Contributing

If you would like to contribute to this project, please follow the standard open-source contribution guidelines and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

