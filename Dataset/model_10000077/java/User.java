





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String firstname;
    private String id;
    private String password;
    private String username;
    private String lastname;
    private String attribute;



    public User(
        String firstname,        String id,        String password,        String username,        String lastname,        String attribute    ) {
        this.firstname = firstname;
        this.id = id;
        this.password = password;
        this.username = username;
        this.lastname = lastname;
        this.attribute = attribute;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}