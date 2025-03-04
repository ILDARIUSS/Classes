import sys
import os
import pytest
# Импорты должны идти после настройки PYTHONPATH
from main import Product, Category

# Принудительно добавляем `src` в PYTHONPATH перед импортами
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_product_creation():
    """Проверяем создание продукта."""
    product = Product("Ноутбук", "Мощный ноутбук", 70000.50, 5)
    assert product.name == "Ноутбук"
    assert product.price == 70000.50
    assert product.quantity == 5


def test_product_creation_with_zero_quantity():
    """Проверяем выброс ошибки при создании продукта с нулевым количеством."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Карандаш", "Обычный карандаш", 10, 0)


def test_average_price():
    """Проверяем расчет средней цены товаров в категории."""
    category = Category("Электроника", "Электронные устройства")
    category.add_product(Product("Телефон", "Смартфон", 30000, 2))
    category.add_product(Product("Ноутбук", "Лэптоп", 60000, 3))

    assert category.average_price() == (30000 + 60000) / 2


def test_average_price_empty_category():
    """Проверяем расчет средней цены при отсутствии товаров."""
    category = Category("Пустая категория", "Нет товаров")
    assert category.average_price() == 0
