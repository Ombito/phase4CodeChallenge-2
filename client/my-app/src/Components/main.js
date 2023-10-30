import React, { useEffect, useState } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch('http://localhost:4000/restaurants')
      .then((res) => res.json())
      .then((data) => setRestaurants(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div>
        <h1>Restaurants</h1>
        <ul>
            {restaurants.map((restaurant) => (
                <li key={restaurant.id}>
                <h2>{restaurant.name}</h2>
                <p>Address: {restaurant.address}</p>
                </li>
            ))}
        </ul>
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
