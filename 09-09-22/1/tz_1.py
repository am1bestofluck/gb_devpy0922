from enum import Enum,auto
class Side(Enum):
    left=auto()
    right=auto()
from array_init import Semi_array

def turn_array(array_i:list)->list:
    '''отзеркаливаем список'''
    array_m=[]
    for i in array_i:
        array_m.append(None)
    buffer=0
    _len_i=len(array_i)
    mediana=_len_i%2
    cross_view_index={Side.left:0,Side.right:0}
    if _len_i<=1:
        array_m=array_i
        return array_m
        pass
    if mediana:
        init_index_step=1
    else:
        init_index_step=0.5
        pass
    cross_view_index[Side.left]=int(_len_i/2-init_index_step)#tyt fiks!
    cross_view_index[Side.right]=int(_len_i/2+init_index_step)#tyt fiks!
    while cross_view_index[Side.left]>=0:
        buffer=array_i[cross_view_index[Side.left]]
        array_m[cross_view_index[Side.left]]=array_i[cross_view_index[Side.right]]
        array_m[cross_view_index[Side.right]]=buffer
        cross_view_index[Side.left]-=1
        cross_view_index[Side.right]+=1
    return array_m

def main():
    _init=Semi_array(size=10,limit=100,unique=True)
    mirrored_init=turn_array(_init.get_instance())
    print(f'main:       {str(_init.get_instance())}')
    print(f'mirrored     {str(mirrored_init)}')
if __name__=='__main__':
    main()