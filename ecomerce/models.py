from django.db import models
from decimal import Decimal
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)

class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,related_name='products')
    tags = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices,default=0)
    shipping_cost = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    def discount_percentage(self):
        if self.discount > 0:
            self.price = self.price * (Decimal(1 - self.discount/100))
        return self.price
    def __str__(self):
        return self.name

class Customer(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


