from django.test import TestCase
from olisaude.models import Costumer

# Create your tests here.

class SimpleTest(TestCase):
    def createCostumer(self):
        Costumer.objects.create(
            first_name='Sabino', last_name='Afonso', 
            gender='M'
        )

    #HearthProblem.objects.create(name='Diabetes', degree='Low', code_costumer=p)
