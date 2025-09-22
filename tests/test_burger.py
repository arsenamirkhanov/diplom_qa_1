import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bun import Bun
from burger import Burger

# Ручной мок для ингредиента
class MockIngredient:
    def __init__(self, name="Lettuce", price=0.5, type_="FILLING"):
        self._name = name
        self._price = price
        self._type = type_
    def get_price(self):
        return self._price
    def get_name(self):
        return self._name
    def get_type(self):
        return self._type

# Ручной мок для булочки
class MockBun:
    def get_price(self):
        return 2.0
    def get_name(self):
        return "Sesame"

class TestBurger:

    def test_set_buns_and_get_price(self):
        burger = Burger()
        bun = MockBun()
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.get_price() == 4.0

    def test_add_and_remove_ingredient(self):
        burger = Burger()
        bun = MockBun()
        ingredient = MockIngredient()
        burger.set_buns(bun)

        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        bun = MockBun()
        burger.set_buns(bun)

        ing1 = MockIngredient("A", 1)
        ing2 = MockIngredient("B", 1)
        ing3 = MockIngredient("C", 1)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1]

    def test_get_price_with_ingredients(self):
        burger = Burger()
        bun = MockBun()
        ing1 = MockIngredient("Cheese", 1)
        ing2 = MockIngredient("Tomato", 0.5)

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert burger.get_price() == 5.5

    def test_get_receipt(self):
        burger = Burger()
        bun = MockBun()
        ing1 = MockIngredient("Cheese", 1, "FILLING")
        ing2 = MockIngredient("Ketchup", 0.5, "SAUCE")

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        receipt = burger.get_receipt()
        expected_lines = [
            "(==== Sesame ====)",
            "= filling Cheese =",
            "= sauce Ketchup =",
            "(==== Sesame ====)",
            "Price: 5.5"
        ]
        for line in expected_lines:
            assert line in receipt
