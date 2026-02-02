from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),      # корзина
    path('orders/', include('orders.urls')),  # заказы
    path('users/', include('users.urls')),    # пользователи
    path('', include('products.urls')),       # главная и товары (ПОСЛЕДНИЙ!)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)