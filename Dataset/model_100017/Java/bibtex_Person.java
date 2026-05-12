





import java.util.List;
import java.util.ArrayList;

public class bibtex_Person  {

    private String firstName;
    private String secondName;
    private String lastName;



    public bibtex_Person(
        String firstName,        String secondName,        String lastName    ) {
        this.firstName = firstName;
        this.secondName = secondName;
        this.lastName = lastName;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getSecondname() {
        return secondName;
    }

    public void setSecondname(String secondName) {
        this.secondName = secondName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }


}