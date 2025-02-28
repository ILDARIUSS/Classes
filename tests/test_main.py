import sys
import os
from main import BaseProduct, Product, Smartphone, LawnGrass

# Принудительно добавляем `src` в PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_base_product_abstract():
    """Проверяем, что нельзя создать экземпляр BaseProduct."""
    try:
        BaseProduct("Продукт", "Описание", 100, 5)
    except TypeError:
        assert True
    else:
        assert False, "Ожидалось исключение TypeError для абстрактного класса"


def test_print_mixin(capsys):
    """Проверяем, что PrintMixin печатает сообщение о создании объекта."""
    _ = Smartphone(
        "iPhone", "Флагманский смартфон", 100000, 5, "Высокая",
        "14 Pro", 256, "Черный"
    )
    captured = capsys.readouterr()
    assert "Создан объект Smartphone" in captured.out


def test_product_creation():
    product = Product("Ноутбук", "Мощный ноутбук", 70000.50, 5)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный ноутбук"
    assert product.price == 70000.50
    assert product.quantity == 5


def test_smartphone_creation():
    smartphone = Smartphone(
        "iPhone", "Флагманский смартфон", 100000, 5, "Высокая",
        "14 Pro", 256, "Черный"
    )
    assert smartphone.name == "iPhone"
    assert smartphone.model == "14 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawngrass_creation():
    grass = LawnGrass(
        "Green Grass", "Газонная трава", 500, 20,
        "Россия", 14, "Зеленый"
    )
    assert grass.name == "Green Grass"
    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "Зеленый"
