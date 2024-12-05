from django.urls import path, include
<<<<<<< HEAD
from rest_framework import routers

from Product.viewset.product_viewset import ProductViewSet
from Product.viewset.category_viewset import CategoryViewSet


router = routers.SimpleRouter()
router.register(r"product", ProductViewSet, basename="Product")
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
=======
from rest_framework import routes

from Product import viewset


router = routes.SimpleRouter()
router.register(r'product', viewset.OrderViewset, basename='product')


urlpatterns = [
    path('', include(router.urls))
]
>>>>>>> df4847e5 (Incluindo o viewset)
