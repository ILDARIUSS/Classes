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
        """
        super().__init__()  # Вызываем __init__ PrintMixin
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


class Smartphone(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        efficiency: str, model: str, memory: int, color: str
    ):
        """Инициализация смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} ({self.model}), {self.price} руб., "
            f"цвет {self.color}"
        )


class LawnGrass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        country: str, germination_period: int, color: str
    ):
        """Инициализация газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} (из {self.country}), {self.price} руб., "
            f"цвет {self.color}"
        )
