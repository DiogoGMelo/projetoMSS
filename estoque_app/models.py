from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import now


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Evite armazenar senhas diretamente
    role = models.CharField(max_length=50, choices=[('manager', 'Manager'), ('seller', 'Seller')])

    def __str__(self):
        return self.name

    @classmethod
    def get_user(cls, user_id):
        try:
            return cls.objects.get(id=user_id)
        except cls.DoesNotExist:
            return None


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    marketplace = models.JSONField()
    
    def update_details(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description
        self.save()

    def adjust_stock(self, quantity: int):
        if self.stock_quantity + quantity < 0:
            raise ValueError("Stock cannot be negative")
        self.stock_quantity += quantity
        self.save()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_date = models.DateTimeField(default=now)
    products = models.ManyToManyField(Product, through="OrderProduct")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def calculate_total(self):
        self.total_price = sum(item.quantity * item.product.price for item in self.orderproduct_set.all())
        self.save()

    def __str__(self):
        return f"Order {self.id} - Total: {self.total_price}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Seller(User):
    role = "seller"
    class Meta:
        proxy = True

    def register_product(self, product: Product):
        product.save()
        return True

    def update_stock(self, product_id: int, quantity: int):
        product = Product.objects.get(id=product_id)
        product.adjust_stock(quantity)
        return True


class Manager(User):
    role = "manager"
    class Meta:
        proxy = True

    def view_financial_report(self):
        # Implementar lógica de relatório financeiro
        return "Financial report"
    
    def register_product(self, product: Product):
        product.save()
        return True

    def update_stock(self, product_id: int, quantity: int):
        product = Product.objects.get(id=product_id)
        product.adjust_stock(quantity)
        return True
