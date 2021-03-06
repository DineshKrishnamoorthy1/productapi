
from rest_framework import serializers
from product1.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_category', 'created_date', 'available_items')
