from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),                 # Home page

    path('apply-promo/', views.apply_promo, name='apply_promo'),  # Added trailing slash
]
