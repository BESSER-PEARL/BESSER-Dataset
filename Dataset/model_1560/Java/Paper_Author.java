





import java.util.List;
import java.util.ArrayList;

public class Paper_Author  {

    private String email;
    private String lastname;
    private String firstname;



    public Paper_Author(
        String email,        String lastname,        String firstname    ) {
        this.email = email;
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }


}