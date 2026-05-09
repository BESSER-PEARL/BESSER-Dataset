





import java.util.List;
import java.util.ArrayList;

public class model_organization_User extends OrgUnit {

    private String lastName;
    private String firstName;
    private String email;



    public model_organization_User(
        String lastName,        String firstName,        String email    ) {
        super(
        );
        this.lastName = lastName;
        this.firstName = firstName;
        this.email = email;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}