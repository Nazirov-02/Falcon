from django.db import models
from decimal import Decimal
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):

    class Choices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=100,default="",)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=14)
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(choices=Choices.choices, default=Choices.ONE)
    shipping = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def discount_percentage(self):
        if self.discount > 0:
            price = self.price * Decimal((1 - self.discount / 100))
            price_rounded = price.quantize(Decimal('0.01'))
            return price_rounded
        return self.price

class Img(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.product.name
    def image_url(self):
        return self.image.url