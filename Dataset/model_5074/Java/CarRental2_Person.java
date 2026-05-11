





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Person  {

    private int lastname;
    private int age;
    private boolean isMarried;
    private int firstname;



    public CarRental2_Person(
        int lastname,        int age,        boolean isMarried,        int firstname    ) {
        this.lastname = lastname;
        this.age = age;
        this.isMarried = isMarried;
        this.firstname = firstname;
    }


    public int getLastname() {
        return lastname;
    }

    public void setLastname(int lastname) {
        this.lastname = lastname;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public boolean getIsmarried() {
        return isMarried;
    }

    public void setIsmarried(boolean isMarried) {
        this.isMarried = isMarried;
    }
    public int getFirstname() {
        return firstname;
    }

    public void setFirstname(int firstname) {
        this.firstname = firstname;
    }


}