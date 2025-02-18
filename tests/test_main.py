import sys
import os
from main import Product, Category  # Импорт исправлен

# Принудительно добавляем `src` в PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_product_creation():
    product = Product("Ноутбук", "Мощный ноутбук", 70000.50, 5)
    assert product.name == "Ноутбук"
    assert product.description == "Мощный ноутбук"
    assert product.price == 70000.50
    assert product.quantity == 5


def test_category_creation():
    category = Category("Бытовая техника", "Различные приборы")
    assert category.name == "Бытовая техника"
    assert category.description == "Различные приборы"
    assert isinstance(category.products, str)


def test_category_product_count():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Игрушки", "Детские игрушки")
    product = Product("Кубики", "Развивающая игрушка", 120.99, 20)

    category.add_product(product)

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product():
    category = Category("Игрушки", "Детские игрушки")
    product = Product("Кубики", "Развивающая игрушка", 120.99, 20)

    category.add_product(product)

    assert "Кубики, 120.99 руб. Остаток: 20 шт." in category.products


def test_add_invalid_product():
    category = Category("Игрушки", "Детские игрушки")

    try:
        category.add_product("не продукт")
    except TypeError as e:
        assert str(e) == "Можно добавлять только объекты класса Product или его наследников"
    else:
        assert False, "Ожидалось исключение TypeError"


def test_price_setter():
    product = Product("Телефон", "Смартфон", 50000, 10)

    product.price = -100
    assert product.price == 50000

    product.price = 30000
    assert product.price == 30000


def test_new_product():
    data = {
        "name": "Планшет",
        "description": "Мощный планшет",
        "price": 35000,
        "quantity": 7
    }
    new_product = Product.new_product(data)

    assert new_product.name == "Планшет"
    assert new_product.description == "Мощный планшет"
    assert new_product.price == 35000
    assert new_product.quantity == 7
