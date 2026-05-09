





import java.util.List;
import java.util.ArrayList;

public class tinylibrary_Person  {

    private String lastName;
    private String firstName;
    private String name;



    public tinylibrary_Person(
        String lastName,        String firstName,        String name    ) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}