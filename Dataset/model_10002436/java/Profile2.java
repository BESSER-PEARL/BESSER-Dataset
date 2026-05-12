





import java.util.List;
import java.util.ArrayList;

public class Profile2  {

    private String firstName;
    private String username;
    private String name;
    private String email;



    public Profile2(
        String firstName,        String username,        String name,        String email    ) {
        this.firstName = firstName;
        this.username = username;
        this.name = name;
        this.email = email;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}