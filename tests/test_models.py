import pytest
from estoque.models import User, Product, Order, OrderProduct, Seller, Manager

@pytest.mark.django_db
def test_create_user():
    user = User(name='João', email='joao@email.com')
    assert str(user) == 'João'

@pytest.mark.django_db
def test_create_product():
    product = Product(name='Teclado', price=100.0, quantity=10)
    assert product.name == 'Teclado'
    assert product.price == 100.0
    assert product.quantity == 10

@pytest.mark.django_db
def test_create_order_product():
    product = Product(name='Mouse', price=50.0, quantity=5)
    order = Order()
    order_product = OrderProduct(product=product, order=order, quantity=2)
    assert order_product.quantity == 2
