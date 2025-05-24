from django.contrib import admin
from django.urls import path, include
from promo_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('promo_app.urls')),
     path('', views.home, name='home'),
     path('email-preview/', views.email_preview, name='email_preview'),

     
]
# https://subham-promo-handler.onrender.com/