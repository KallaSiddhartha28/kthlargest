Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> public class HappyNumber  
{     
    public static int isHappyNumber(int num){  
        int rem = 0, sum = 0;  
          
        while(num > 0){  
            rem = num%10;  
            sum = sum + (rem*rem);  
            num = num/10;  
        }  
        return sum;  
    }  
      
    public static void main(String[] args) {  
        int num = 82;  
        int result = num;  
          
        while(result != 1 && result != 4){  
            result = isHappyNumber(result);  
        }  
          
        if(result == 1)  
            System.out.println(num + " is a happy number");  
        else if(result == 4)  
            System.out.println(num + " is not a happy number");     
    }  
}  