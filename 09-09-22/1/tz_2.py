#а если в массиве сто одинаковых чисел что тогда? Если все одинаковые?
from operator import index
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
    internal_borders=(limits['min']+1,limits['max']-1)
    for index_ in internal_borders:
        sum_o+=core[index_]
    return sum_o

def main():
    example=Semi_array(size=10,limit=100,unique=True)
    list_exa=example.get_instance()
    # list_exa=[83, 15, 81, 28, 77, 17, 31, 49, 24, 80]
    limits_dict=get_extremum_indexes(object=list_exa)
    print(example)
    print(f'list: {str(list_exa)}')
    resolve=get_sum_of_elements(core=list_exa,limits=limits_dict)
    print(resolve)
    q=input('debug')
if __name__=='__main__':
    main()