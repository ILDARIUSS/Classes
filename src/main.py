class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        """
        Инициализация товара.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут с двойным подчеркиванием
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        """Строковое представление товара"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения.
        Складывает полную стоимость всех товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
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

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
