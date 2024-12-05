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
        fields = ['prooduct', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        Product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')

        order = Order.objects.create(**validated_data)
        for product in Product_data:
            order.product.add(product)

        return order