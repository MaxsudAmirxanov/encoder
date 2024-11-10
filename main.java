package encoder;
// import java.util.Scanner;


import java.io.*;
import java.util.*;
import java.nio.charset.StandardCharsets;

// import java.io.File;
// import java.io.FileReader;
// import java.io.IOException;
// import java.util.ArrayList;
// import java.util.List;
// import java.io.*;

class programm {
    public static void main(String[] args){
        boolean loop = true;
        

        

        do{
            System.out.println("Допро пожаловать в Шифратор, выберите действие:"); 

            System.out.println("1) Добаить скрытый шифр в текст.");
            System.out.println("2) Расшифровать скрытый шифр.");
            System.out.println("3) Узнать количество битов, которые можно зашифровать в тексте.");
            System.out.println("4)"); 

            Scanner in = new Scanner(System.in);
            
            int num = in.nextInt();
            
            

            if (num == 1){
                
                
                System.setProperty("file.encoding", "UTF-8");
                

                try {
                    File file = new File("C:/Users/maxsu/OneDrive/Рабочий стол/программы/encoder/input.txt");
         
                    //создаем объект InputStreamReader для объекта File
                    InputStreamReader fr = new InputStreamReader(new FileInputStream(file), "UTF-8");
                    //создаем BufferedReader с существующего InputStreamReader для построчного считывания
                    BufferedReader reader = new BufferedReader(fr);

                    List<String> lines = new ArrayList<String>();
                    String NAME1 = reader.readLine();
                    do{
                        lines.add(NAME1);
                        NAME1 = reader.readLine();
                    }
                    while(NAME1!=null);

                    System.out.println(lines);
                    reader.close();
                    
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                

                String main_encoder = in.next();
                System.out.println("qwerty1");
                System.out.println(main_encoder);
                Cryptography numberSystem = new Cryptography(null, null, null, null);
                
                String a = numberSystem.text_to_bits(main_encoder);
                System.out.println(a);
                System.out.println("qwerty2");
                numberSystem.encryption_letter(a);
                System.out.println(main_encoder);
            }
            
            else if (num == 2){
                NumberSystem.decimal_binary(25);
                Cryptography C = new Cryptography(null, null, 35, null);
                System.out.println(C.count_bit);
                // C.encryption_letter();

            }
            else if (num == 3){
                

            }
            else if (num == 4){

            }  
        }
        while (loop == true);
            // in.close();
        
    }           
        
}
class NumberSystem{
    String main_text;
    String main_encoder;
    Integer count_bit;
    String shifr_text_bit;

    public NumberSystem(String main_text, String main_encoder, Integer count_bit, String shifr_text_bit){
        this.count_bit = count_bit;
        this.main_encoder = main_encoder;
        this.main_text = main_text;
        this.shifr_text_bit = shifr_text_bit;
    }
    /**Перерводит число с десятичной сс, в двоичнуюу*/
    public static String decimal_binary(int main_number){
        

        
        main_number = 46;
        List<Integer> a = new ArrayList<Integer>();

        // a.add(0, 1);
        while (main_number != 1){
            
            System.out.println(main_number);
            Integer b = main_number%2;
            a.add(0, b);
            float y = (float)main_number;
            main_number =  (int)y/2;
            System.out.println(main_number);
            // System.out.println(main_number%2);

            if (main_number == 1){
                a.add(0, 1);
            }
        }

            
        System.out.println(a);

        return "123";
    }

    public String text_to_bits(String secretText) {
        byte[] bytes = secretText.getBytes(StandardCharsets.UTF_8);
        StringBuilder binary = new StringBuilder();
        for (byte b : bytes) {
            int val = b;
            System.out.println(val);
            for (int i = 0; i < 8; i++) {
                binary.append((val & 128) == 0 ? 0 : 1);
                val <<= 1;
            }
        }

        return binary.toString();
}

}
class Cryptography extends NumberSystem{
    /**Шивровка текста через буквы */
    // String main_text = this.main_text;
    public Cryptography(String main_text, String main_encoder, Integer count_bit, String shifr_text_bit){
        super(main_text, main_encoder, count_bit, shifr_text_bit);
        // print()
        // this.count_bit = count_bit;
        // this.main_encoder = main_encoder;
        // this.main_text = main_text;
        // this.shifr_text_bit = shifr_text_bit;
        // System.out.println(count_bit);
        // System.out.println("ntcb");

    }
    public void encryption_letter(String bit)  {
        
        // System.out.println(Cryptography.count_bit);
        String text = this.main_text;

        ArrayList<Object> list_bit = new ArrayList<Object>();

 
        for (int i = 0; i < bit.length(); i++) {
            list_bit.add(bit.charAt(i));
        }
 
        System.out.println(list_bit);

        System.out.println(this.count_bit);
        HashMap<String, String> map = new HashMap<>();
        map.put("у","y");
        map.put("о","o");
        map.put("а","a");
        map.put("с","c");
        map.put("р","p");
        map.put("е","e");
        map.put("х","x");
        
        System.out.println(map);
 
        // System.out.println(map.entrySet());
        // System.out.println(map.keySet());
        // System.out.println(map.values());
 
        // ArrayList<String> val =
        //         new ArrayList<>(map.values());
        // System.out.println(val);
 
        // ArrayList<HashMap.Entry> entries =
        //         new ArrayList<>(map.entrySet());
        // System.out.println(entries);
        // for (HashMap.Entry entry : entries) {
        //     System.out.println(entry.getKey());
        // }
 
        // ArrayList<String> keys = new ArrayList<>();
        // keys.addAll(map.keySet());
        // System.out.println(keys);
        

        
        
    }


}
