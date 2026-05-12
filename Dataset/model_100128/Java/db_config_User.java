





import java.util.List;
import java.util.ArrayList;

public class db_config_User extends ServerResource {

    private String firstname;
    private String lastname;
    private String password;



    public db_config_User(
        String firstname,        String lastname,        String password    ) {
        super(
        );
        this.firstname = firstname;
        this.lastname = lastname;
        this.password = password;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}