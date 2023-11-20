from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from olisaude.models import Costumer
from olisaude.serializers import serializer

# Create your views here.

def toListCostumers(request):
    costumers = Costumer.objects.all()
    data = serializer(costumers)
    return JsonResponse(data, safe=False, 
                    json_dumps_params={'indent':4, 'ensure_ascii':True}
                    )

def getCostumer(request, code_costumer):
    costumer = get_object_or_404(Costumer, code=code_costumer)
    if costumer:
        costumer = (costumer,)
    data = serializer(costumer)
    return JsonResponse(data, safe=False, 
                    json_dumps_params={'indent':4, 'ensure_ascii':True}
                    )
    
