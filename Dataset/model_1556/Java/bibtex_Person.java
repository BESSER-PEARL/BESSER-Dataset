





import java.util.List;
import java.util.ArrayList;

public class bibtex_Person  {

    private String secondName;
    private String lastName;
    private String firstName;



    public bibtex_Person(
        String secondName,        String lastName,        String firstName    ) {
        this.secondName = secondName;
        this.lastName = lastName;
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
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}