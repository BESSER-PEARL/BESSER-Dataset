





import java.util.List;
import java.util.ArrayList;

public class company_Employee  {

    private String firstName;
    private String lastName;
    private int age;



    public company_Employee(
        String firstName,        String lastName,        int age    ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}