// define string
public class DuplicateWord{
    public static void main(String[] args){
        String str = "JAVA is a programming language";
        int count;
        // convert the string into lowercase
        str=str.toLowerCase();
        //split the string into words using built-in function
        String words[]=str.split("");
        System.out.println("duplicate words in a given string :" );
        //Logic: loop through each word in the array and compare it with all the other words
        for(int i=0;i<words.length;i++)
        {
            count=1;
            for(int j=i+1;j<words.length;j++){
                if (words[i].equals(words[j]))
                {
                count++;
                //set words[j]to 0 means counting will start from zero.
                words[j]="0";
                }
            }
        }
        



    }
}