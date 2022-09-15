//комментарий в java ставится двумя знаками деления, однострочный
/* а многострочный- /* 
 * при этом vscode почему то ставит " *" в каждой новой строчке...
но она большой роли не играет, вот!
 */
import java.util.Arrays;
class why_hello_world_is_so_wordy{
        public static void main(String[] args) {
            //[2, 5, 13, 7, 6, 4]
            System.out.println("Боже, такая заумь...");
            byte [] numbers ;
            numbers= new byte[6];
            numbers[0]=2;
            numbers[1]=5;
            numbers[2]=13;
            numbers[3]=7;
            numbers[4]=6;
            numbers[5]=4;
            // byte[] secondByteArray =new byte[]{2,5,13,7,6,4};
            // System.out.println("There is another way tho: ");
            // System.out.println("byte[] secondByteArray =new byte[]{2,5,13,7,6,4};");
            int sum;
            byte index;
            sum= 0;
            index=0;
            double size =6.0;
            double average;
            average=0;
            for (index=0; index<size;index++)
                sum+=numbers[index];
            average=sum/size;
            System.out.println("Сумма:" + String.valueOf(sum));
            String output= new String("Средняя по массиву:" + Double.toString(average));
            System.out.println(output);

        //     String separator ;
        //     separator= new String("\n===");
        //     for (int redo=0; redo<3; redo++)
        //         System.out.println(separator);
        //     System.out.println("offtop!");
        //     System.out.println("Declare array with <type of stored items> [] <nameOfVariableCamelcased> ;");
        //     System.out.println("Then allocate memory to it with <nameOfVariableCamelcased>= <type of stored items>[<expected_lenght>]");
        //     System.out.println("Allocate значит выделить:) ну собсно не тайна. Несчастная аллокация памяти кусочками по 120 мб");
        //     System.out.println("которой всё равно не хватает, потому что древний движок не берёт больше 8 гб за раз. Плавали-знаем.");
        //     System.out.println("Но в другом контексте...:)");
        //     System.out.println("This java is absolutely wordy....");
        //     System.out.println("And not only that! You are to compile it with external console...");
        //     System.out.println("And only then you run it with external console too. I swear.");
        //     System.out.println("Single-line comments are written in //<comment>");
        //     System.out.println("Multilined comments start with /*");
        //     System.out.println("and end with");
        //     System.out.println("*/");
        //     System.out.println("newline characters are \\r and \\n");
        // /*}
        // public static void average(String[] args){
        // */
        //     String stringvar ;
        //     stringvar= new String("comment");
        //     System.out.println(stringvar);
        //     /*
        //     int[] intArray = new int[]{ 1,2,3,4,5,6,7,8,9,10 }; 
        //     // Declaring array literal
        //     */
        }
    }