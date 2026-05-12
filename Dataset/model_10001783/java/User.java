





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String location;
    private String email;



    public User(
        String location,        String email    ) {
        this.location = location;
        this.email = email;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}