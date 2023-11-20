from django.contrib import admin
from .models import Costumer, HearthProblem


@admin.register(Costumer)
class CostumerAdmin(admin.ModelAdmin):
    """
        Class Costumer to Admin
    """
    list_display = ['code', 'first_name', 'last_name',
                    'gender', 'birth_date', 'created_date', 
                    'updated_date'
                ]

    list_display_links = ['code']

    list_editable = ['first_name', 'last_name',
                    'gender', 'birth_date', 
                ]
    
    list_per_page = 10
    ordering = ('code',)


@admin.register(HearthProblem)
class HearthProblemAdmin(admin.ModelAdmin):
    """
        Class HearthProblem to Admin
    """
    list_display = ['name', 'degree', 'code_costumer']
    list_display_links = ['code_costumer']
    list_editable = ['name', 'degree']
    
    list_per_page = 10
    ordering = ('code_costumer',)