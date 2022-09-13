from array_init import Semi_array
def get_extremum_indexes(object:list)->dict:#можно запаковать в интерфейс класса=\
    '''Нахождение индексов максимального и минимального элемента массива'''
    support_min_max={
        'min':{'value':object[0],'index':object.index(object[0])},
        'max':{'value':object[0],'index':object.index(object[0])}
        }
    output={}
    for _lookup in object:# здесь можно ещё один for для min max-ключей 
        # чтобы не дублировать код в строках 10,11 и 13,14
        if _lookup>support_min_max['max']['value']:
            support_min_max['max']['value']=_lookup
            support_min_max['max']['index']=object.index(_lookup)
        if _lookup<support_min_max['min']['value']:
            support_min_max['min']['value']=_lookup
            support_min_max['min']['index']=object.index(_lookup)
    output={'min':support_min_max['min']['index'],'max':support_min_max['max']['index']}
    return output

def main():
    example=Semi_array(size=100,limit=1000000,unique=True)
    print(example)
    core=example.get_instance()
    print(core)
    
    minmax=get_extremum_indexes(core)
    print(minmax)
    borders=example.borders
    assert minmax['min']==core.index(borders['min']) and\
        minmax['max']==core.index(borders['max'])
if __name__=='__main__':
        main()