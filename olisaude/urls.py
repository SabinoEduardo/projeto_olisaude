from django.urls import path
from olisaude import views

app_name = 'costumer'

urlpatterns = [
   
    path('', views.home, name='home'),

    # Costumer
    path('costumers/', views.toListCostumers, name='list_costumers'), # list costumer
    path('costumers/<int:code_costumer>/', views.getCostumer, name='get_costumer'), # get one costumer
    path('costumers/create/', views.createCostumer, name='creater'), # crater costumer
    path('costumers/<int:code_costumer>/update/', views.updateCostumer, name='update'), # update costumer
]
