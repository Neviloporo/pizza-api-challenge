from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {
            'id': r.id,
            'name': r.name,
            'address': r.address
        } for r in restaurants
    ]), 200


@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [
            {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            } for rp in restaurant.restaurant_pizzas
        ]
    }), 200


@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
