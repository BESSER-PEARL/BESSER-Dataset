





import java.util.List;
import java.util.ArrayList;

public class CarRental_Person  {

    private int age;
    private String lastname;
    private String firstname;
    private boolean isMarried;



    public CarRental_Person(
        int age,        String lastname,        String firstname,        boolean isMarried    ) {
        this.age = age;
        this.lastname = lastname;
        this.firstname = firstname;
        this.isMarried = isMarried;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public boolean getIsmarried() {
        return isMarried;
    }

    public void setIsmarried(boolean isMarried) {
        this.isMarried = isMarried;
    }


}