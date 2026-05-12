





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String username;
    private String about;
    private String password;





    private User user;


    public Profile(
        String username,        String about,        String password    ) {
        this.username = username;
        this.about = about;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}