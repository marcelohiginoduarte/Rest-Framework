from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('boolstore/(?P<version>(v1|v2))', include('order.urls')),
    re_path('boolstore/(?P<version>(v1|v2))', include('Product.urls'))
]
