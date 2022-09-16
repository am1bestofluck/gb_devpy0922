//переводим блок схему в код
import java.util.Arrays;
import java.util.Random;
class GoRepeat{
    static void calculate_repetions_of_max(int[] numbers){
        //Старт #считаем количество элементов с максимальным значением
        //Принимаем массив //совсем как в тз, только любо
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
        while (index<_len) {
            //проверяем элемент на максимальность :))) numbers[index]>maximum? #if
            if (numbers[index]>maximum){
                //if true: Он больше известного максимума: задаём новый максимум и и обнуляем счётчик
                //maximum=numbers[index] count_maximal=1
                maximum=numbers[index];
                count_maximal=1;
            }
            // if False /*Он не больше максимума, но может быть он ему равен? numbers[index]==maximum? */
            else { 
                if (numbers[index]==maximum){
                    // if True
                        /*Накидываем +1 к счётчику максимальных значений #count_maximal+=1 //count_maximal++ */
                        count_maximal++;}
                }

                    // if False: pass
            //шагаем по циклу на шаг вперёд #index+=1//index++1
            index++;}
        System.out.println("Максимальное значение "+Integer.toString(maximum)+ " встретилось "+Integer.toString(count_maximal)+" раз.");
        //выводим count_maximal
        //Финиш //#4
    }
    public static void main(String[] args){
        int[] static_array;
        static_array=new int[]{1,8,3,8,2,6,8,8};
        System.out.println("Задание");
        System.out.println(Arrays.toString(static_array));
        calculate_repetions_of_max(static_array);
        System.out.println("Рандомим массив чуть подлиннее");
        int [] random_array;
        random_array = new int[100];
        Random random_int=new Random();
        int upper_limit;
        upper_limit=10;
        byte index=0;
        for (index=0;index<random_array.length;index++){
            random_array[index]=random_int.nextInt(upper_limit);
        }
        System.out.println(Arrays.toString(random_array));
        calculate_repetions_of_max(random_array);


   }
}