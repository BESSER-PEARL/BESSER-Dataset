





import java.util.List;
import java.util.ArrayList;

public class library3Simplified_Customer  {

    private String firstName;
    private String lastName;



    public library3Simplified_Customer(
        String firstName,        String lastName    ) {
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