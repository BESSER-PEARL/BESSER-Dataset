





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String username;





    private User user;


    public Profile(
        String username    ) {
        this.username = username;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}