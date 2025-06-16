from flask import Blueprint, jsonify, request
from models import db
from models.restaurant_pizza import RestaurantPizza
from models.pizza import Pizza
from models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(new_rp.pizza_id)
        restaurant = Restaurant.query.get(new_rp.restaurant_id)

        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": pizza.id,
            "restaurant_id": restaurant.id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201

    except ValueError as ve:
        return jsonify({ "errors": [str(ve)] }), 400
    except Exception as e:
        return jsonify({ "errors": ["Invalid data"] }), 400
