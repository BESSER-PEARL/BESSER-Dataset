





import java.util.List;
import java.util.ArrayList;

public class Profile_Page  {

    private String password;
    private String username;





    private User user;


    public Profile_Page(
        String password,        String username    ) {
        this.password = password;
        this.username = username;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}