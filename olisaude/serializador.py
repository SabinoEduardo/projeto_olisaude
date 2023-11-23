# File content method serializers
# type: ignore

from django.http import JsonResponse

def serializerCostumers(costumer, hearth_problems=None):
    """
        This method serializer a object send for views functions
    """
    
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
                dict_problems['id'] = hearth.id
                dict_problems['name'] = hearth.name
                dict_problems['degree'] = hearth.degree
                list_problems.append(dict_problems.copy())

            dict_costumer['hearth_problems'] = list_problems

        dict_costumer['birth_date'] = value.birth_date
        dict_costumer['created_date'] = value.created_date
        dict_costumer['updated_date'] = value.updated_date

        list_costumers.append(dict_costumer.copy())
    return list_costumers


def serializerproblems(problem):
    dict_problem = dict()
    data = list()
    
    code_costumer = problem.code_costumer.code
    full_name_costumer = f'{problem.code_costumer.first_name} {problem.code_costumer.last_name}'
    data.append({'code_costumer':code_costumer, 'full_name_costumer': full_name_costumer})
    
    dict_problem['id'] = problem.id
    dict_problem['name'] = problem.name
    dict_problem['degree'] = problem.degree

    problems = {'health of problems':dict_problem.copy()}

    data.append(problems)
    return data