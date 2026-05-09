





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_Customer  {

    private String lastName;
    private String firstName;



    public se_hotelsystem_Customer(
        String lastName,        String firstName    ) {
        this.lastName = lastName;
        this.firstName = firstName;
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