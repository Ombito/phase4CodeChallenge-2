import React, { useEffect, useState } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/restaurants')
      .then((res) => res.json())
      .then((data) => setRestaurants(data))
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
