





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String about;
    private String password;
    private String username;





    private User user;


    public Profile(
        String about,        String password,        String username    ) {
        this.about = about;
        this.password = password;
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