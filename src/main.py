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
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для списка товаров.
        Возвращает строку со всеми товарами в формате:
        "Название продукта, 80 руб. Остаток: 15 шт."
        """
        return "\n".join(
            [
                f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
                for p in self._products
            ]
        )


if __name__ == "__main__":
    category1 = Category("Электроника", "Гаджеты и устройства")
    product1 = Product("Смартфон", "Мощный телефон", 50000.99, 10)
    product2 = Product("Ноутбук", "Игровой ноутбук", 120000, 5)

    category1.add_product(product1)
    category1.add_product(product2)

    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")

    print("\nСписок товаров в категории:")
    print(category1.products)

    product1.price = -500  # Должно вывести сообщение об ошибке
    print(f"Цена смартфона: {product1.price}")

    new_product_data = {
        "name": "Планшет",
        "description": "Мощный планшет",
        "price": 35000,
        "quantity": 7
    }
    new_product = Product.new_product(new_product_data)
    print(
        "\nСоздан новый продукт: "
        f"{new_product.name}, {new_product.price} руб., "
        f"Остаток: {new_product.quantity} шт."
    )
