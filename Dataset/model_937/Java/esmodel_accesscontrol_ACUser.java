





import java.util.List;
import java.util.ArrayList;

public class esmodel_accesscontrol_ACUser extends ACOrgUnit {

    private String firstName;
    private String lastName;



    public esmodel_accesscontrol_ACUser(
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