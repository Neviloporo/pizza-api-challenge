from flask import Flask
from flask_migrate import Migrate
from models import db
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
