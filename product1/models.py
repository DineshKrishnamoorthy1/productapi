from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30, blank=False, default='')
    created_date = models.DateTimeField(null=True)
    available_items = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']