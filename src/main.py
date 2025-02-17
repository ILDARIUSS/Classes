class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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
        self.products = []

        # Обновляем счетчики
        Category.category_count += 1

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        :param product: Объект класса Product
        """
        self.products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    # Проверка работы классов
    category1 = Category("Электроника", "Гаджеты и устройства")
    product1 = Product("Смартфон", "Мощный телефон", 50000.99, 10)

    category1.add_product(product1)

    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")
