//c#
//должно работать на windows/macos
//принимаем ...2... ...случайных... числа.
int num_a=new Random().Next(1,10);//1,2,3..9
Console.WriteLine(num_a);
int num_b=new Random().Next(11,20);//11,12,13..19
Console.WriteLine(num_b);
int outputval=0;
outputval=num_a+num_b;
Console.WriteLine(outputval);
//складываем
//выводим результат