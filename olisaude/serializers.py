# File content method serializers
# type: ignore

from django.http import JsonResponse

def serializerCostumers(costumer, hearth_problems=None):
    """
        This method serializer a object send for views functions
    """
    if not isinstance(costumer, dict):

        dict_costumer = dict()
        list_costumers = list()
        dict_problems = dict()
        list_problems = list()

        for value in costumer:
            dict_costumer['code'] = value.code
            dict_costumer['first_name'] = value.first_name
            dict_costumer['last_name'] = value.last_name
            dict_costumer['gender'] = value.gender
            
            if hearth_problems != None:
                for hearth in hearth_problems:
                    dict_problems['name'] = hearth.name
                    dict_problems['degree'] = hearth.degree
                    list_problems.append(dict_problems.copy())

                dict_costumer['hearth_problems'] = list_problems

            dict_costumer['birth_date'] = value.birth_date
            dict_costumer['created_date'] = str(value.created_date.strftime("%d/%m/%Y %H:%M:%S"))
            dict_costumer['updated_date'] = str(value.updated_date.strftime("%d/%m/%Y %H:%M:%S"))

            list_costumers.append(dict_costumer.copy())
        data = list_costumers
    else:
        data = costumer
    data = JsonResponse(data, safe=False, json_dumps_params={'indent':4, 'ensure_ascii':False})
    return data


