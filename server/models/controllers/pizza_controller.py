from flask import Blueprint, jsonify
from server.models import db
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)


@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [
        {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        for pizza in pizzas
    ]
    return jsonify(result), 200
