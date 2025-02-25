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
        if not isinstance(other, type(self)):
            raise TypeError("Складывать можно только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str
    ):
        """
        Инициализация смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str
    ):
        """
        Инициализация газонной травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
