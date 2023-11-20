from django.urls import path
from olisaude import views

urlpatterns = [
    path('', views.toListCostumers, name='list_costumers'),
    path('costumers/<int:code_costumer>/', views.getCostumer, name='get_costumer'),
]
