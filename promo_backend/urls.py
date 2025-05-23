from django.contrib import admin
from django.urls import path, include
from promo_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('promo_app.urls')),
     path('', views.home, name='home'),
]
