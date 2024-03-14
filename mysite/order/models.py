from django.db import models


# Create your models here.
class Option(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    options = models.ManyToManyField(Option)

    def __str__(self):
        return self.name
    
class Drink(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    
    def __str__(self):
        return self.name

    
class Shoppingcart(models.Model):
    name = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    count = models.DecimalField(max_digits=8, decimal_places=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.name

class Order_Item(models.Model):
    order_number = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    count = models.DecimalField(max_digits=8, decimal_places=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    order_number = models.CharField(max_length=50)
    order_date = models.DateTimeField(auto_now_add=True)
    order_items = models.ManyToManyField(Order_Item)
    total=models.DecimalField(max_digits=8,decimal_places=0)

    def __str__(self):
        return self.order_number
