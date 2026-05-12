





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String username;
    private String password;
    private String attribute;



    public User(
        String username,        String password,        String attribute    ) {
        this.username = username;
        this.password = password;
        this.attribute = attribute;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}