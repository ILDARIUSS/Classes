import sys
import os
from main import Product, Category  # Импорт исправлен

# Принудительно добавляем `src` в PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_product_str():
    product = Product("Ноутбук", "Мощный ноутбук", 70000.50, 5)
    assert str(product) == "Ноутбук, 70000.5 руб. Остаток: 5 шт."


def test_category_str():
    category = Category("Бытовая техника", "Различные приборы")
    product1 = Product("Миксер", "Кухонный миксер", 5000, 3)
    product2 = Product("Пылесос", "Мощный пылесос", 15000, 2)

    category.add_product(product1)
    category.add_product(product2)

    assert str(category) == "Бытовая техника, количество продуктов: 5 шт."


def test_product_add():
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 120000, 5)

    assert product1 + product2 == (50000 * 10) + (120000 * 5)


def test_product_add_type_error():
    product = Product("Телефон", "Смартфон", 50000, 10)
    try:
        product + "не продукт"
    except TypeError as e:
        assert str(e) == "Складывать можно только объекты класса Product"
    else:
        assert False, "Ожидалось исключение TypeError"


def test_category_product_count():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Игрушки", "Детские игрушки")
    product = Product("Кубики", "Развивающая игрушка", 120.99, 20)

    category.add_product(product)

    assert Category.category_count == 1
    assert Category.product_count == 1
