#а если в массиве сто одинаковых чисел что тогда? Если все одинаковые?
from array_init import Semi_array
from tz_0 import get_extremum_indexes

def get_sum_of_elements(core:list,limits:dict)->int:
    '''считаем сумму значений членов массива которые расположены между индексами
     предельных значений массива'''
    #output={'min':support_min_max['min']['index'],'max':support_min_max['max']['index']}
    assert 'min' in limits and 'max' in limits and len(limits)==2# лучше класс сделать
    sum_o=0
    if limits['min']-limits['max'] in [-1,0,1]:
        return sum_o
    internal_borders=(limits['min'],limits['max'])
    match internal_borders[0]>internal_borders[1]:
        case True:
            step=-1
        case False:
            step=1
    route=range(internal_borders[0],internal_borders[1],step)
    for index_ in route:
        sum_o+=core[index_]
    sum_o=sum_o-core[route[0]]
    return sum_o

def main():
    example=Semi_array(size=10,limit=20,unique=True)
    list_exa=example.get_instance()
    limits_dict=get_extremum_indexes(object=list_exa)
    print(limits_dict)
    print(example)
    print(f'list: {str(list_exa)}')
    resolve=get_sum_of_elements(core=list_exa,limits=limits_dict)
    print('#',resolve)
if __name__=='__main__':
    main()  