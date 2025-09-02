"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(5) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False



    def test_product_buy(self, product):
        product.buy(100)
        assert product.quantity == 900

        # TODO напишите проверки на метод buy



    def test_product_buy_more_than_av(self, product):
        with pytest.raises(ValueError) as e:
            product.buy(1001)
            assert str(e.value) == 'товара нет в наличии'


class TestCart:

    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        assert cart.products[product] ==5
        cart.add_product(product, 5)
        assert cart.products[product] ==10

    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.remove_product(product,2)
        assert cart.products[product] ==3
        cart.remove_product(product,4)
        assert not cart.products

    def test_clear(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.clear()
        assert not cart.products


    def test_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500
        cart.remove_product(product,2)
        assert cart.get_total_price() == 300

    def test_cart_buy(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 995
        assert not cart.products

    def test_cart_buy_not_enough(self, product):
        cart = Cart()
        cart.add_product(product, 1001)
        with pytest.raises(ValueError) as e:
            cart.buy()
            assert "не хватает на складе" in str(e.value)
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """