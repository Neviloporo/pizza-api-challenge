from server.app import create_app
from server.models import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    print("Seeding database...")

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Pineapple, Ham")

    db.session.add_all([p1, p2, p3])

    r1 = Restaurant(name="Luigi's Pizza", address="123 Mario Lane")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Studio St")
    r3 = Restaurant(name="Nairobi Slice", address="789 Kenyatta Ave")

    db.session.add_all([r1, r2, r3])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=8, pizza_id=p1.id, restaurant_id=r2.id)
    rp4 = RestaurantPizza(price=12, pizza_id=p3.id, restaurant_id=r3.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

    print("Done seeding!")
