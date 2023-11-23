# type: ignore
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse
from olisaude.models import Costumer, HearthProblem
from olisaude import serializador, forms
from django.db.models import Q


# Constat 
DATA = {
        'status_code': 405,
        'message': 'Method Not Allowed'
    }


def home(request):
    """
        This method return status code 200 and a messagem.
    """
    data = {
            'status_code': 200,
            'message': 'API Olisaude'
        }
    return JsonResponse(data, safe=False, json_dumps_params={'indent':4})
       

def toListCostumers(request):
    """
        To list all costumers or show the message "No Content" if database is empity
    """
    costumers = Costumer.objects.all() # get all objetcts
    if costumers:
        data = serializador.serializerCostumers(costumer=costumers)
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
    
    # if database is empity
    data = {
        'status_code': 204,
        'message': 'No Content'
    }
    return JsonResponse(data, safe=False, json_dumps_params={'indent':4})


def getCostumer(request, code):
    try:
        costumer = Costumer.objects.get(code=code)
        problems = HearthProblem.objects.filter(code_costumer__exact=costumer.code)

        data = serializador.serializerCostumers((costumer,), hearth_problems=problems)
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
    
    except:
        data = {
        'status_code': 404,
        'message': 'Costumer Not Found'
        }
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4})
    

def searchCostumer(request):
    """
        Get a costumer or show a message error if costumer not exist in DB
    """

    value = request.GET.get('q', '').strip()
    if value == '':
        return redirect('costumer:list_costumers')
    
    costumer = Costumer.objects.filter(
        Q(first_name__contains=value) |
        Q(last_name__contains=value)
    ) # try filter a costumer with first name or last name

    if costumer:
        data = serializador.serializerCostumers(costumer=costumer)
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
    
    data = {
        'status_code': 404,
        'message': 'Costumer Not Found'
    }
    return JsonResponse(data, safe=False, json_dumps_params={'indent':4})
    

@csrf_exempt
def createCostumer(request):
    """
        Create a costumer or return a error if form not is valid
    """
    if request.method == "POST":
        form = forms.CostumerForm(request.POST)
        if form.is_valid(): # check if data of form is valid
            costumer = form.save()
            return redirect('costumer:get_costumer', code=costumer.code)
        
        # if form not is valid
        msg_error = form.errors
        return JsonResponse(msg_error, safe=False, json_dumps_params={'indent':4})
    
    # if request.method not is POST
    return JsonResponse(DATA, safe=False, json_dumps_params={'indent':4})


@csrf_exempt
def updateCostumer(request, code_costumer):
    """
        update datas of costumers withoud hearth problems
    """
    try:
        costumer = Costumer.objects.get(code=code_costumer)

        if request.method in 'POST':
            form = forms.CostumerForm(request.POST, instance=costumer)
            if form.is_valid(): # valida se os dados são válidos
                form.save()
                return redirect('costumer:get_costumer', code=costumer.code)
            
            msg_error = form.errors
            return JsonResponse(msg_error, safe=False, json_dumps_params={'indent':4})
        
        data = serializador.serializerCostumers(costumer=(costumer,))
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
    except:
        data = {
        'status_code': 404,
        'message': 'Costumer Not Found'
        }
        return JsonResponse(data, safe=False, json_dumps_params={'indent':4})


@csrf_exempt     
def addHearthProblems(request):

    """
        Add a health problem
    """
    if request.method == "POST":
        form = forms.HearthProblemForm(request.POST)
        code = request.POST.get('code_costumer')

        if form.is_valid():
            name = request.POST.get('name')
            degree = request.POST.get('degree')
            code_costumer = request.POST.get('code_costumer')

            problems = HearthProblem.objects.filter(
                Q(name__exact=name) &
                Q(degree__exact=degree) &
                Q(code_costumer__exact=code_costumer)
            )

            if not problems:
                form.save()
                return redirect('costumer:get_costumer', code=code_costumer)

            msg_alert = {'msg':'This health problem is already associated with this client'}
            return JsonResponse(msg_alert, safe=False, json_dumps_params={'indent':4})
        
        # form is not valid
        costumer = Costumer.objects.filter(code__exact=code)
        if not costumer:
            data = {
                'status_code': 404,
                'message': f'Object code_costumer={code} not exist'
            }
            return JsonResponse(data)
        
        msg_error = form.errors
        return JsonResponse(msg_error, safe=False, json_dumps_params={'indent':4})
    
    # if method.request not is POST
    return JsonResponse(DATA, safe=False, json_dumps_params={'indent':4})
    

@csrf_exempt 
def updateHearthProblems(request, id_problem):

    # try get a costumer with code

    problem = HearthProblem.objects.get(id=id_problem)
    if request.method == 'POST':
        form = forms.HearthProblemForm(request.POST, instance=problem)
        if form.is_valid():
            problem = form.save()
            code = problem.code_costumer.code
            return redirect('costumer:get_costumer', code=code)
        msg_error = form.errors
        return JsonResponse(msg_error, safe=False, json_dumps_params={'indent':4})
    data = serializador.serializerproblems(problem)
    return JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
