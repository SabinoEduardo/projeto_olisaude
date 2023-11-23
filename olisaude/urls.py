from django.urls import path
from olisaude import views

app_name = 'costumer'

urlpatterns = [
   
    path('', views.home, name='home'),

    # Costumer
    path('costumers/', views.toListCostumers, name='list_costumers'), # list costumer
    path('costumers/get/<int:code>', views.getCostumer, name='get_costumer'), # get one costumer
    path('costumers/search/', views.searchCostumer, name='filter_costumer'), # filter costumers
    path('costumers/create/', views.createCostumer, name='creater'), # crater costumer
    path('costumers/<int:code_costumer>/update/', views.updateCostumer, name='update'), # update costumer

    # Hearth Problems
    path('problems/register/', views.addHearthProblems, name='register'), # crater health
    path('problems/<int:id_problem>/update/', views.updateHearthProblems, name='update'), 
    # update health
]
