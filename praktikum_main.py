from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient

def main():
    database = Database()
    burger = Burger()

    buns = database.available_buns()
    ingredients = database.available_ingredients()

    burger.set_buns(buns[0])
    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    burger.move_ingredient(2, 1)
    burger.remove_ingredient(3)

    print(burger.get_receipt())

if __name__ == "__main__":
    main()
