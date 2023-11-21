# type: ignore
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from olisaude.models import Costumer, HearthProblem
from olisaude import serializers, forms
from django.http import JsonResponse

def home(request):
    data = {
            'status_code': 200,
            'message': 'API Olisaude'
        }
    return serializers.serializerCostumers(data)


def toListCostumers(request):
    """
        To list all costumers or show a message error
    """
    costumers = Costumer.objects.all()
    if not costumers:
        data = {
            'status_code': 204,
            'message': 'No Content'
        }

    data = serializers.serializerCostumers(costumers)
    return data


def getCostumer(request, code_costumer):
    """
        Get a costumer or show a message error
    """
    try:
        costumer = Costumer.objects.get(code=code_costumer)
        problems = HearthProblem.objects.filter(code_costumer__exact=costumer.code)
        costumer = (costumer, )
    except:
        data = {
            'status_code': 404,
            'message': 'Costumer Not Found'
        }
    data = serializers.serializerCostumers(costumer=costumer, hearth_problems=problems)
    return data


@csrf_exempt
def createCostumer(request):
    """
        Create a costumer or return a error if form not is valid
    """
    if request.method ==  "POST":
        form = forms.CostumerForm(request.POST)
        if form.is_valid(): # valida se os dados são válidos
            costumer = form.save()
            return redirect('costumer:get_costumer', code_costumer=costumer.code)
    msg_error = form.errors
    return JsonResponse(msg_error, safe=False, json_dumps_params={'indent':4})
    

@csrf_exempt
def updateCostumer(request, code_costumer):
    """
        update datas of costumers withoud hearth problems
    """
    try:
        costumer = Costumer.objects.get(code=code_costumer)

        if request.method == 'POST':
            form = forms.CostumerForm(request.POST, instance=costumer)
            if form.is_valid(): # valida se os dados são válidos
                form.save()
                return redirect('costumer:get_costumer', code_costumer=costumer.code)
        date = form.errors
        return JsonResponse(date, safe=False, json_dumps_params={'indent':4})
    
    except:
        date = {'status_code': 404,
                'message': 'Costumer Not Found',
                }
        return JsonResponse(date, safe=False, json_dumps_params={'indent':4})
        

