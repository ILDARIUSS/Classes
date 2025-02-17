import pytest
from main import Product, Category


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
    assert isinstance(category.products, list)


def test_category_product_count():
    Category.category_count = 0  # Сброс счетчика
    Category.product_count = 0  # Сброс счетчика

    category = Category("Игрушки", "Детские игрушки")
    product = Product("Кубики", "Развивающая игрушка", 120.99, 20)

    category.add_product(product)

    assert Category.category_count == 1
    assert Category.product_count == 1
