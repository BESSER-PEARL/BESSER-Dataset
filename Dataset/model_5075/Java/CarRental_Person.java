





import java.util.List;
import java.util.ArrayList;

public class CarRental_Person  {

    private int age;
    private String firstname;
    private String lastname;
    private boolean isMarried;



    public CarRental_Person(
        int age,        String firstname,        String lastname,        boolean isMarried    ) {
        this.age = age;
        this.firstname = firstname;
        this.lastname = lastname;
        this.isMarried = isMarried;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
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


}