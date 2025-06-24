# Pizza Restaurant API

A RESTful API for managing a pizza restaurant, built using Flask and SQLAlchemy. No frontend required — test everything using **Postman**.


## Project Setup

### Create Virtual Environment & Install Dependencies


pipenv install flask flask_sqlalchemy flask_migrate

pipenv shell


### 🛠 Database Setup


export FLASK_APP=server/app.py

flask db init

flask db migrate -m "Initial migration"

flask db upgrade


###  Seeding Data

Edit `server/seed.py` with initial data and run:


python server/seed.py



## Models

### Restaurant

- `id`: Integer, primary key
- `name`: String
- `address`: String
- **Relationships**: Has many RestaurantPizzas (cascade deletes enabled)

### Pizza

- `id`: Integer, primary key
- `name`: String
- `ingredients`: String
- **Relationships**: Has many RestaurantPizzas

### RestaurantPizza (Join Table)

- `id`: Integer, primary key
- `price`: Integer (must be between 1 and 30)
- `pizza_id`: ForeignKey
- `restaurant_id`: ForeignKey
- **Relationships**: Belongs to Pizza and Restaurant


##  API Endpoints

### `GET /restaurants`

Returns list of all restaurants.

### `GET /restaurants/<int:id>`

Returns restaurant info and its pizzas.

- **404** if not found:  
  `{ "error": "Restaurant not found" }`

### `DELETE /restaurants/<int:id>`

Deletes the restaurant and associated RestaurantPizzas.

- **204 No Content** if successful  
- **404** if not found

### `GET /pizzas`

Returns a list of all pizzas.

### `POST /restaurant_pizzas`

Creates a RestaurantPizza.  
**Example Request:**

  <!-- json -->
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}


**Success Response:**

<!-- json -->
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "address3"
  }
}




## Testing with Postman

1. Open Postman
2. Import `challenge-1-pizzas.postman_collection.json`
3. Test all routes

---

## Routes Deliveries

## GET All Restaurants
![All the restaurants](./screenshots/Screenshot%20from%202025-06-24%2011-33-47.png)

## GET All Pizzas
![All the pizzas](./screenshots/Screenshot%20from%202025-06-24%2011-34-04.png)

  If there is an error
  ![erro](./screenshots/Screenshot%20from%202025-06-24%2011-58-58.png)

## Delete Pizzas
![deletes](./screenshots/Screenshot%20from%202025-06-24%2012-00-50.png)
