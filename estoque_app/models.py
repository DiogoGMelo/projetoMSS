from django.db import models

# Create your models here.
"""
class User {
    - id: int
    - name: str
    - email: str
    - role: str
    + login(email: str, password: str): bool
    + logout(): void
}
"""
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)

    def login(self, email: str, password: str) -> bool:
        pass

    def logout(self) -> None:
        pass

"""
class Product {
    - productId: int
    - name: str
    - price: float
    - stockQuantity: int
    - description: str
    + updateDetails(name: str, price: float, description: str): void
    + adjustStock(quantity: int): bool
}
"""
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stockQuantity = models.IntegerField()
    description = models.TextField()

    def updateDetails(self, name: str, price: float, description: str) -> None:
        pass

    def adjustStock(self, quantity: int) -> bool:
        pass

"""class Order {
    - orderId: int
    - orderDate: datetime
    - products: List[Product]
    - totalPrice: float
    + calculateTotal(): float
    + addProduct(product: Product): void
    + removeProduct(productId: int): void
}"""

class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateTimeField()
    products = models.ManyToManyField('Product')
    totalPrice = models.FloatField()

    def calculateTotal(self) -> float:
        pass

    def addProduct(self, product: Product) -> None:
        pass

    def removeProduct(self, productId: int) -> None:
        pass

"""
class Seller {
    - sales: List[Order]
    + registerProduct(product: Product): bool
    + updateStock(productId: int, quantity: int): bool
    + viewSalesReport(): Report
}
"""
class Seller(models.Model):
    sales = models.ManyToManyField('Order')

    def registerProduct(self, product: Product) -> bool:
        pass

    def updateStock(self, productId: int, quantity: int) -> bool:
        pass

    def viewSalesReport(self) -> str:
        pass

"""
class Manager {
    - users: List[User]
    + addUser(user: User): bool
    + removeUser(userId: int): bool
    + viewFinancialReport(): FinancialReport
    + manageProducts(): void
}
"""
class Manager(models.Model):
    users = models.ManyToManyField(User)

    def addUser(self, user: User) -> bool:
        pass

    def removeUser(self, userId: int) -> bool:
        pass

    def viewFinancialReport(self) -> str:
        pass

    def manageProducts(self) -> None:
        pass

