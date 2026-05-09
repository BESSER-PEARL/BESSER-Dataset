





import java.util.List;
import java.util.ArrayList;

public class esmodel_accesscontrol_ACUser extends ACOrgUnit {

    private String lastName;
    private String firstName;



    public esmodel_accesscontrol_ACUser(
        String lastName,        String firstName    ) {
        super(
        );
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