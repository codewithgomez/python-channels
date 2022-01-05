from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


class Customers(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_age = models.FloatField()
    
