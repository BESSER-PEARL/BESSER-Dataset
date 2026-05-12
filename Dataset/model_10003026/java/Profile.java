





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String about;
    private String username;
    private String password;





    private User user;


    public Profile(
        String about,        String username,        String password    ) {
        this.about = about;
        this.username = username;
        this.password = password;
    }


    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}