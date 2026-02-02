import java.util.concurrent.ThreadLocalRandom;
public class randomnumbers {
    public static int getrandomvalue(String[] args){
    return ThreadLocalRandom.current().nextInt((Min, Max+1));
    }
    public static void main(String[] args){
        int min=1,max=100;
        System.out.println("random value between"+min+"and"+max+":"+getrandomvalue(Min,max));
    }
    
}
