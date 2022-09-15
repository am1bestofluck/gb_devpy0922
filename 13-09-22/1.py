def get_arithmetic_mean(_collection:list)->float|None:
    '''Найти среднее арифметическое среди всех элементов массива [2, 5, 13, 7, 6, 4]'''
    for value in _collection:
        if not isinstance(value,float) and not isinstance(value,int):
            print(f'collection must be numbers, not {str(type(value))}!')
            return 
        pass
    _len=len(_collection)
    average_o=0
    _sum=0
    _index=0
    while True:
        if _len==_index:
            break
        _sum+=_collection[_index]
        _index+=1
    average_o=round(_sum/_len,2)
    match _len<10:
        case True:
            print(f'среднее арифметическое для {str(_collection)}: {str(average_o)}')
        case False:
            print(f'среднее арифметическое для {str(_collection[0])}..{str(_collection[-1])}: {str(average_o)}')
    return average_o

def main():
    control_values=[2, 5, 13, 7, 6, 4]
    response=get_arithmetic_mean(control_values)
    correct=round(6.1666,2)
    assert response==correct
    waste=[True,'asd']
    noneval=get_arithmetic_mean(waste)
    assert noneval is None

if __name__=='__main__':
    main()