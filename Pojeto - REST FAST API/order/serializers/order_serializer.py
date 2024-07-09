from rest_framework import serializers

from Product.models import Product
from Product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    Product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()


    def get_total(self, instance):
        total = sum([Product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model = Product
        fields = ['prooduct', 'total']