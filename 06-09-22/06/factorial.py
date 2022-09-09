class Factorial():
    '''находим факториал числа\n'''
    def __init__(self,number_i=None,comment=''):
        'мусор на входе не допускается'
        if isinstance(number_i,int):
            if number_i>=0:#интернет говорит что число- натуральное
                self.__number_m=number_i
                pass
            else:
                self.__askbase()
        else:
            self.__askbase()
        self.__number_m=int(self.__number_m)
        self.description=comment
        self.__math()
    def __askbase(self)->str:
        self.__number_m=''
        while not self.__number_m.isdecimal():
            self.__number_m=input('дай число пож, натуральное')
    def __math(self)->int:
        '''расчётная часть. Как её сделать через генератор? И возможно ли?'''
        self.__list=list(range(1,self.__number_m+1,1))
        self.out=1
        for to_multipy in self.__list:
            self.out*=to_multipy
    def __repr__(self)->str:
        print(self.description)
        return(f'факториал числа {str(self.__number_m)}: {self.out}')
    
def main():
    print(Factorial.__doc__)
    w=Factorial(10,comment='получаем аргумент от api')
    print(w)
    q=Factorial(comment='Принимаем аргумент от пользователя')
    print(q)
    for test_garbage in [':)',None,False,{1:True},set(),[]]:#bool проходит потому что нулёвый. Это нужно исправлять?
        test_=Factorial(comment=Factorial.__init__.__doc__,number_i=test_garbage)
        print(test_)
if __name__=='__main__':
    main()
