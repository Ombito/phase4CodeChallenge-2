import React, { useEffect, useState } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/restaurants')
      .then((res) => res.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);  
    
  useEffect(() => {
    fetch('http://127.0.0.1:5555/pizzas')
      .then((res) => res.json())
      .then((data) => setPizzas(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
        <ol>
            {restaurants.map((restaurant) => (
                <li key={restaurant.id}>
                <h2>Name: {restaurant.name}</h2>
                <p>Address: {restaurant.address}</p>
                </li>
            ))}
        </ol>
        <br></br>
        <br></br>
        <h1>PIZZAS</h1>
        <ol>
            {pizzas.map((pizza) => (
                <li key={pizza.id}>
                <h2>Name: {pizza.name}</h2>
                <p>Ingredients: {pizza.ingredients}</p>
                </li>
            ))}
        </ol>
    </div>
    
  );
}

const Main = () => {
  return (
    <div>
      <h1>RESTAURANTS</h1>
      <RestaurantList />
    </div>
  );
}

export default Main;
