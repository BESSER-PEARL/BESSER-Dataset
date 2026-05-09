





import java.util.List;
import java.util.ArrayList;

public class library_Person extends Addressable {

    private String firstName;
    private String lastName;



    public library_Person(
        String firstName,        String lastName    ) {
        super(
        );
        this.firstName = firstName;
        this.lastName = lastName;
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


}