from math import lcm as mcm

def numbers_option(request):
    list_chart = request.GET.get('numbers').split(sep=",")
    array = []
    for i in list_chart:
        array.append(int(i))

    result = mcm(*array)
    return {
            'numbers': array,
            'result': result
        }

def one_number(request):
    number=int(request.GET.get('number'))
    return {
            'number': number,
            'result': number + 1
        }