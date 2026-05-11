





import java.util.List;
import java.util.ArrayList;

public class persons_Person  {

    private String lastName;
    private String id;
    private String firstName;



    public persons_Person(
        String lastName,        String id,        String firstName    ) {
        this.lastName = lastName;
        this.id = id;
        this.firstName = firstName;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}