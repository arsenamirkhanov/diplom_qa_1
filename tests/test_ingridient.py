import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ingredient import Ingredient

class TestIngredient:

    def test_creation(self):
        ing = Ingredient("FILLING", "Cheese", 1.5)
        assert ing.type == "FILLING"
        assert ing.name == "Cheese"
        assert ing.price == 1.5

    def test_get_price(self):
        ing = Ingredient("SAUCE", "Ketchup", 0.5)
        assert ing.get_price() == 0.5

    def test_get_name(self):
        ing = Ingredient("FILLING", "Lettuce", 0.3)
        assert ing.get_name() == "Lettuce"

    def test_get_type(self):
        ing = Ingredient("SAUCE", "Mayo", 0.4)
        assert ing.get_type() == "SAUCE"
