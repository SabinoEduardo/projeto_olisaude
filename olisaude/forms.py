from django import forms
from olisaude.models import Costumer, HearthProblem


class CostumerForm(forms.ModelForm):

    class Meta:
        model = Costumer
        fields = [
                    'first_name', 'last_name',
                    'gender', 'birth_date'
                ]
        
class HearthProblemForm(forms.ModelForm):
    class Meta:
        model = HearthProblem
        fields = ['name', 'degree', 'code_costumer']