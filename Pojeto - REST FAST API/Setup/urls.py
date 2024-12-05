from django.contrib import admin
from django.urls import path, include, re_path
<<<<<<< HEAD
import debug_toolbar
from rest_framework.authtoken.views import obtain_auth_token
=======
>>>>>>> df4847e5 (Incluindo o viewset)

urlpatterns = [
    
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    re_path('bookstore/(?P<version>(v1|v2))/', include('order.urls')),
    re_path('bookstore/(?P<version>(v1|v2))/', include('Product.urls')),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    ]
=======
    re_path('boolstore/(?P<version>(v1|v2))', include('order.urls')),
    re_path('boolstore/(?P<version>(v1|v2))', include('product.urls'))
]
>>>>>>> df4847e5 (Incluindo o viewset)
