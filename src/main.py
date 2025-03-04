from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, product_data):
        """Абстрактный метод для создания нового продукта"""
        pass


class PrintMixin:
    """Класс-миксин, печатающий информацию о создании объекта."""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект {class_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(PrintMixin, BaseProduct):
    """Класс товаров, наследующий базовый продукт и использующий миксин."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ):
        """
        Инициализация продукта.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество в наличии
        :raises ValueError: Если количество товара равно 0
        """
        super().__init__()  # Вызываем __init__ PrintMixin

        if quantity == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self._price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения.
        Складывает полную стоимость всех товаров на складе.
        """
        if not isinstance(other, type(self)):
            raise TypeError("Складывать можно только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания продукта из словаря.
        :param product_data: Словарь с данными о товаре
        :return: Экземпляр Product
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )


class Category:
    """Класс для хранения категорий товаров."""

    category_count = 0  # Счетчик категорий
    product_count = 0  # Счетчик товаров

    def __init__(self, name: str, description: str):
        """
        Инициализация категории.
        :param name: Название категории
        :param description: Описание категории
        """
        self.name = name
        self.description = description
        self._products = []  # Приватный список товаров

        # Обновляем счетчик категорий
        Category.category_count += 1

    def add_product(self, product):
        """
        Добавляет товар в категорию.
        :param product: Объект класса Product или его наследников
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product "
                "или его наследников"
            )
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для списка товаров.
        Возвращает строку со всеми товарами в формате:
        "Название продукта, 80 руб. Остаток: 15 шт."
        """
        return "\n".join(str(p) for p in self._products)

    def average_price(self):
        """
        Метод для вычисления среднего ценника товаров в категории.
        :return: Средняя цена товаров или 0, если товаров нет.
        """
        try:
            total_price = sum(p.price for p in self._products)
            return total_price / len(self._products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
