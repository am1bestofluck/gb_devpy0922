def sort_handmade(numbers_i:list)->list:
    numbers_m=numbers_i
    size=len(numbers_m)
    index=0
    max_idx=0
    _max=numbers_m[max_idx]
    while index<size:
        if numbers_m[index]>_max:
            max_idx=index
            _max=numbers_m[index]
        index+=1
    numbers_m[max_idx]=numbers_m[size-1]
    numbers_m[size-1]=_max
    # print(numbers)
    return numbers_m

numbers=[2,5,13,7,6,4]
check=numbers.sort()
while check!=numbers:
    print(f'b4:{numbers}')
    numbers=sort_handmade(numbers_i=numbers)
    print(f'after:{numbers}')