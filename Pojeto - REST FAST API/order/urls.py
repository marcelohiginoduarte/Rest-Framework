from django.urls import path, include
<<<<<<< HEAD
from rest_framework.routers import SimpleRouter

from order.viewset.order_viewset import OrderViewSet


router = SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')
=======
from rest_framework import routes

from order import viewset


router = routes.SimpleRouter()
router.register(r'order', viewset.OrderViewset, basename='order')
>>>>>>> df4847e5 (Incluindo o viewset)


urlpatterns = [
    path('', include(router.urls))
]