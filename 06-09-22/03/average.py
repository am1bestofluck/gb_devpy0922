#считаем среднюю скажем так четырёх чисел
class Average():
    def __init__(self,collection_i=None,limit=4) -> None:
        self.limit=limit
        self.average=0
        if not isinstance(collection_i,list) and not isinstance(collection_i,tuple) and not isinstance(collection_i,range):
            self.__data=self.__gather_numbers()
        else:
            for walk in collection_i:
                if not isinstance(walk,int) and not isinstance(walk,float) and not self.check_decimal_string(walk):
                    self.__data=self.__gather_numbers()
                    break
                pass
        try:
            if self.__data:
                pass
        except AttributeError:
            self.__data=collection_i
        if len(self.__data)>self.limit:
            self.__cut_to_limit()
            pass
        elif len(self.__data)<self.limit:
            self.__data=self.__gather_numbers()
            pass
        else:
            pass
        self.__math()
    def __cut_to_limit(self)->None:
        if len(self.__data)!=self.limit:
            self.__data=self.__data[:self.limit]
    def __gather_numbers(self)->list:
        '''Собираем переменные. 4 так 4.'''
        output_list=[]
        while len(output_list)!=self.limit:
            add_this=input('число дай пож')
            if self.check_decimal_string(add_this):
                output_list.append(int(add_this))
            else:
                print(f'{add_this}- не число!')
            pass
        return output_list
    '''Собираем циферки'''
    def __math(self)->float:
        self.average=sum(self.__data)/len(self.__data)
        pass
    def check_decimal_string(self,value_i:str)->bool:
        '''ищем строковые цифры.
        Можно было бы импортировать pyinputplus в принципе... и Стив Макконел говорит что всё что можно одолжить-
        писать не нужно. Но Мы же тут учимся.'''
        output_bool=False
        if isinstance(value_i,str):
            if value_i.isdecimal():
                output_bool=True
                pass
            pass
        return output_bool
    def __repr__(self) -> str:
        return f'Средняя арифметическая чисел {str(self.__data)}: {str(self.average)}'
    def get_instance(self)->float:
        return self.average

def main():
    print('считаем среднюю от пользователя')
    q=Average()
    print(q)
    args=[
        [30,70,10,90],
        range(1,301,10),
        (1,2,3,4),
        50,
        'привет мир',
        None
        ]
    for incoming_data in args:
        print(f'считаем среднюю, на входе: {str(incoming_data)}')
        q=Average(incoming_data)
        print(q)

if __name__=='__main__':
    main()