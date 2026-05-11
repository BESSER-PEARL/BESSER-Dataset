





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Person  {

    private String lastname;
    private boolean isMarried;
    private String firstname;
    private int age;



    public CarRental2_Person(
        String lastname,        boolean isMarried,        String firstname,        int age    ) {
        this.lastname = lastname;
        this.isMarried = isMarried;
        this.firstname = firstname;
        this.age = age;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public boolean getIsmarried() {
        return isMarried;
    }

    public void setIsmarried(boolean isMarried) {
        this.isMarried = isMarried;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}