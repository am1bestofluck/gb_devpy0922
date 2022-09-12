import random
class Semi_array():
    def __doc__():
        return 'создаём рандомный список интов от 0 до limit размерностью size'
    def __init__(self,size:int,limit:int,unique:bool):
        self.size=size
        self.limit=limit
        self.limits=(0,0)#init
        self.unique=unique
        if self.unique:
            assert self.size<self.limit
            pass
        assert self.size>0
        self.__math()
    def __math(self):
        self.__calculate()
        self.__get_limits()

    def __calculate(self):
        '''расчётная часть'''
        self.__body=[]
        if self.unique:
            self.__body_set=set()
            while len(self.__body_set)!=self.size:
                self.__body_set.add(random.choice(range(0,self.limit)))
            self.__body=list(self.__body_set)
            random.shuffle(self.__body)
        else:
            for redo in range(self.size):
                self.__body.append(random.choice(range(0,self.limit)))
        pass
    def get_instance(self):
        '''выдаём сам массив'''
        return self.__body
    def __get_limits(self):
        '''шпаргалка по пределам'''
        self.__min=min(self.__body)
        self.__max=max(self.__body)
        self.borders={'min':self.__min,'max':self.__max}
    def __repr__(self):
        return f'массив из {self.size} значений. Пределы: {self.borders["min"]}:{self.borders["max"]}.'

