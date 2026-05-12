





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String attribute;
    private String password;
    private String firstname;
    private String lastname;
    private String id;
    private String username;



    public User(
        String attribute,        String password,        String firstname,        String lastname,        String id,        String username    ) {
        this.attribute = attribute;
        this.password = password;
        this.firstname = firstname;
        this.lastname = lastname;
        this.id = id;
        this.username = username;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}