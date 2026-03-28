from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    product_image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.IntegerField()
    contact_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name