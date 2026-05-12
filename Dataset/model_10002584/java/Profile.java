





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String Password;
    private String Username;
    private String About;





    private User user;


    public Profile(
        String Password,        String Username,        String About    ) {
        this.Password = Password;
        this.Username = Username;
        this.About = About;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getAbout() {
        return About;
    }

    public void setAbout(String About) {
        this.About = About;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}