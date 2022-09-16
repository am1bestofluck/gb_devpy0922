import array_init
def count_maximal(list_i:list)->None:
    index=0
    max_={'val':list_i[index],'count_output':0}
    while True:
        if index==len(list_i):
            break
        if list_i[index]>max_['val']:
            max_['val']=list_i[index]
            max_['count_output']=1
            pass
        else:
            if list_i[index]==max_['val']:
                max_['count_output']+=1
            else:
                pass
        index+=1
    print(f"Максимальное значение {max_['val']} встретилось {max_['count_output']} раз.")
def main():
    tz=[1,8,3,8,2,6,8,8]
    print(tz)
    count_maximal(tz)
    random_array=array_init.Semi_array(size=100,limit=10,unique=False)
    print(random_array.get_instance())
    count_maximal(random_array.get_instance())
if __name__=='__main__':
    main()