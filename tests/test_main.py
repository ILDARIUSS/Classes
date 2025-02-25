import sys
import os
from main import Product, Smartphone, LawnGrass, Category

# Принудительно добавляем `src` в PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


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


def test_product_add():
    smartphone1 = Smartphone(
        "Samsung", "Смартфон", 50000, 10, "Средняя",
        "S22", 128, "Белый"
    )
    smartphone2 = Smartphone(
        "iPhone", "Смартфон", 120000, 5, "Высокая",
        "14 Pro", 256, "Черный"
    )

    assert smartphone1 + smartphone2 == (50000 * 10) + (120000 * 5)


def test_product_add_type_error():
    smartphone = Smartphone(
        "iPhone", "Флагманский смартфон", 100000, 5, "Высокая",
        "14 Pro", 256, "Черный"
    )
    grass = LawnGrass(
        "Green Grass", "Газонная трава", 500, 20,
        "Россия", 14, "Зеленый"
    )

    try:
        smartphone + grass
    except TypeError as e:
        assert (
            str(e) == "Складывать можно только объекты одного класса"
        )
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


def test_add_invalid_product():
    category = Category("Электроника", "Гаджеты и устройства")

    try:
        category.add_product("не продукт")
    except TypeError as e:
        assert (
            str(e) == "Можно добавлять только объекты класса "
            "Product или его наследников"
        )
    else:
        assert False, "Ожидалось исключение TypeError"
