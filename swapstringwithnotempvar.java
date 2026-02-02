import java.util.*;
public class swapstringwithnotempvar {
  public static void main(String[] args){
    String a ="hello there";
    String b="this is janhvi";
    System.out.println("strings before swap :a="+a+"b="+b);
    a=a+b;
    b=a.substring(0,a.length()-b.length());
    a=a.substring(b.length());
    System.out.println("strings after swap:"+a+"and b="+b);

  } 
}
