from app import db, Restaurant, Pizza

def seed():
    # Create restaurants
    dominion_pizza = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    pizza_hut = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create pizzas
    cheese_pizza = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni_pizza = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add pizzas to restaurants
    dominion_pizza.pizzas.append(cheese_pizza)
    dominion_pizza.pizzas.append(pepperoni_pizza)
    pizza_hut.pizzas.append(cheese_pizza)

    # Add to session and commit
    db.session.add(dominion_pizza)
    db.session.add(pizza_hut)
    db.session.commit()

if __name__ == '__main__':
    seed()
