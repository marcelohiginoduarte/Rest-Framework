from django.urls import path, include
from rest_framework import routes

from Product import viewset


router = routes.SimpleRouter()
router.register(r'product', viewset.OrderViewset, basename='product')


urlpatterns = [
    path('', include(router.urls))
]