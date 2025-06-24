from flask import Blueprint, request, jsonify
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)


@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data['price'])
        pizza_id = int(data['pizza_id'])
        restaurant_id = int(data['restaurant_id'])

        if price < 1 or price > 30:
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return jsonify({"error": "Pizza or Restaurant not found"}), 404

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
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

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400


@restaurant_pizza_bp.route('/', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    result = []
    for rp in restaurant_pizzas:
        result.append({
            "id": rp.id,
            "price": rp.price,
            "pizza": {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            },
            "restaurant": {
                "id": rp.restaurant.id,
                "name": rp.restaurant.name,
                "address": rp.restaurant.address
            }
        })
    return jsonify(result), 200
