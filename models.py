class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity



    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True
        else:
            return False


        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """


    def buy(self, quantity):
        if not self.check_quantity(quantity):
            raise ValueError('товара нет в наличии')
        self.quantity -= quantity

        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """


    def __hash__(self):
        return hash(self.name + self.description) #скливание имени и описания продукта -> необходимо для словаря в классе Cart


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """


    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            raise ValueError ('товара нет в корзине')
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count



        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """


    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return sum(product.price * count for product, count in  self.products.items())

    def buy(self):
        for product in self.products:
            if not product.check_quantity(self.products[product]):
                raise ValueError(f'Товара "{product.name}" не хватает на складе')
            else:
                product.buy(self.products[product])
        self.products = {}





        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
