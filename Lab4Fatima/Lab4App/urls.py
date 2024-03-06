from django.urls import path
from . import views

urlpatterns = [
    path('', views.defaultPath, name='default'),
    path('<int:num>/', views.priceCalculation, name='priceCalc'),
    path('taxrate/', views.taxrate, name='taxrate')
]