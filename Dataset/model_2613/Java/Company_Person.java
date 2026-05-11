





import java.util.List;
import java.util.ArrayList;

public class Company_Person  {

    private String lastname;
    private String firstname;



    public Company_Person(
        String lastname,        String firstname    ) {
        this.lastname = lastname;
        this.firstname = firstname;
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


}