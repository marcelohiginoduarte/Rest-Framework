from django.urls import path, include
from rest_framework import routes

from order import viewset


router = routes.SimpleRouter()
router.register(r'order', viewset.OrderViewset, basename='order')


urlpatterns = [
    path('', include(router.urls))
]