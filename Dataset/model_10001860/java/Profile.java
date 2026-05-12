





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String password;
    private String username;
    private String interests;





    private User user;


    public Profile(
        String password,        String username,        String interests    ) {
        this.password = password;
        this.username = username;
        this.interests = interests;
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
    public String getInterests() {
        return interests;
    }

    public void setInterests(String interests) {
        this.interests = interests;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}