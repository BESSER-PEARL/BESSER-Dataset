





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String password;
    private String lastname;
    private String username;
    private String id;
    private String attribute;
    private String firstname;



    public User(
        String password,        String lastname,        String username,        String id,        String attribute,        String firstname    ) {
        this.password = password;
        this.lastname = lastname;
        this.username = username;
        this.id = id;
        this.attribute = attribute;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }


}