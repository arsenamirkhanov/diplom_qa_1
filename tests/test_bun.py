import sys
import os

# Добавляем корень проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bun import Bun

class TestBun:

    def test_init(self):
        bun = Bun(name="Sesame", price=1.5)
        assert bun.name == "Sesame"
        assert bun.price == 1.5

    def test_get_name(self):
        bun = Bun(name="WholeWheat", price=2.0)
        assert bun.get_name() == "WholeWheat"

    def test_get_price(self):
        bun = Bun(name="Brioche", price=2.5)
        assert bun.get_price() == 2.5
