from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_launches, name='new-launches'),
    path('new_phones', views.new_phones, name='new-phones'),
    path('popular_products', views.popular_products, name='popular-products'),
    path('best_selling', views.best_selling, name='best-selling')
]