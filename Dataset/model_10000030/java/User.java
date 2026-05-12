





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private String location;



    public User(
        String email,        String location    ) {
        this.email = email;
        this.location = location;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}