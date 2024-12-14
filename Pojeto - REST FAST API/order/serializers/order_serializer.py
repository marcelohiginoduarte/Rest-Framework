from rest_framework import serializers

from order.models import Order
from Product.models import Product
from Product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
<<<<<<< HEAD
        model = Order
        fields = ["product", "total", "user", "products_id"]
        extra_kwargs = {"product": {"required": False}}

    def create(self, validated_data):
        product_data = validated_data.pop("products_id")
        user_data = validated_data.pop("user")

        order = Order.objects.create(user=user_data)
        for product in product_data:
=======
        model = Product
        fields = ['prooduct', 'total', 'user', 'products_id']
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        Product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')

        order = Order.objects.create(**validated_data)
        for product in Product_data:
>>>>>>> df4847e5 (Incluindo o viewset)
            order.product.add(product)

        return order