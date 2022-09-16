//переводим блок схему в код
class GoRepeat{
    public static void main(String[] args){
        //Старт #считаем количество элементов с максимальным значением

        //Принимаем массив //совсем как в тз, только любой
        int[] numbers;
        numbers=new int[]{1,8,3,8,2,6,8,8};

        /*Задаём сопроводительные переменные
        оно же- declare -> allocate*/
        //index=0
        //maximum=numbers[index]
        //count_maximal=0
        //_len=numbers.lenght
        //numbers=[...]
        int index,maximum,count_maximal,_len;
        index=0;
        maximum=numbers[index];
        count_maximal=0;
        _len=numbers.length;

        //пока не прошли весь массив //index>_len-1?
        while (index<_len) do

            //проверяем элемент на максимальность :))) numbers[index]>maximum? #if
            if (numbers[index]>maximum){
                //if true: Он больше известного максимума: задаём новый максимум и и обнуляем счётчик
                //maximum=numbers[index] count_maximal=1
                maximum=numbers[index];
                count_maximal=1;
            }
            // if False /*Он не больше максимума, но может быть он ему равен? numbers[index]==maximum? */
            else {
                
            }
                    // if True
                        /*Накидываем +1 к счётчику максимальных значений #count_maximal+=1 //count_maximal++ */
                    // if False: pass
            //шагаем по циклу на шаг вперёд #index+=1//index++1
        
        //выводим count_maximal
        //Финиш //#4
    }
}