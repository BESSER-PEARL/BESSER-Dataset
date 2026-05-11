





import java.util.List;
import java.util.ArrayList;

public class db_config_User extends ServerResource {

    private String password;
    private String lastname;
    private String firstname;



    public db_config_User(
        String password,        String lastname,        String firstname    ) {
        super(
        );
        this.password = password;
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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