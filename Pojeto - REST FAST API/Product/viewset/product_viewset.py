<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet

from Product.models import Product
from Product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("id")
=======
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Product.models import Product
from Product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    queryset - Product.objects.all()
>>>>>>> df4847e5 (Incluindo o viewset)
