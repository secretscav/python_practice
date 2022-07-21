
import java.util.*;

public class Main{
    public static void main(String[] args){
        Mamals person1 = new Mamals("secretscav", 23, "Japanese", true, true, false);
        Mamals person2 = new Mamals("kim", 34, "Korean", false, true, false);
        Mamals person3 = new Mamals("charley", 45, "Indian", true, false, false);
        person1.introduce();
        person1.draw();
        person1.sing();
        person3.dance();

        System.out.println("======================================");
        person2.introduce();
        person2.draw();
        person2.sing();
        person2.dance();

        System.out.println("=======================================");
        person3.introduce();
        person3.draw();
        person3.sing();
        person3.dance();
    }

}

class Mamals{
    String name;
    int age;
    String nationality;
    boolean candraw;
    boolean cansing;
    boolean candance;
    public Mamals(String name, int age, String nationality, boolean candraw, boolean cansing, boolean candance){
        this.name = name;
        this.age = age;
        this.nationality = nationality;
        this.candraw = candraw;
        this.cansing = cansing;
        this.candance = candance;
    }
   
    public void introduce(){
      System.out.println("Hi my name is: " + this.name +", I am " + this.age +" years old" +", My nationality is: " + this.nationality);
    }

    public void draw(){
        if(candraw){
            System.out.println("I can draw");
        }
        else{
            System.out.println("I can't draw");
        }
    }

    public void sing(){
        if(cansing){
            System.out.println("I can sing");
        }
        else{
            System.out.println("I can't sing");
        }
    }
    
    public void dance(){
        if(candance){
            System.out.println("I can dance");
        }
        else{
            System.out.println("I can't dance");
        }
    }
}