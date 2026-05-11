





import java.util.List;
import java.util.ArrayList;

public class CarRental2_Person  {

    private String firstname;
    private String lastname;
    private boolean isMarried;
    private int age;



    public CarRental2_Person(
        String firstname,        String lastname,        boolean isMarried,        int age    ) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.isMarried = isMarried;
        this.age = age;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
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
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}