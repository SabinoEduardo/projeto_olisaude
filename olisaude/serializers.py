# File content method serializers


def serializer(data):
    dict_costumer = dict()
    list_costumers = list()
    for value in data:
        dict_costumer['code'] = value.code
        dict_costumer['first_name'] = value.first_name
        dict_costumer['last_name'] = value.last_name
        dict_costumer['gender'] = value.gender
        dict_costumer['birth_date'] = value.birth_date
        dict_costumer['created_date'] = str(value.created_date.strftime("%d/%m/%Y %H:%M:%S"))
        dict_costumer['updated_date'] = str(value.updated_date.strftime("%d/%m/%Y %H:%M:%S"))

        list_costumers.append(dict_costumer.copy())
    return list_costumers