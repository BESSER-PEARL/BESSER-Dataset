





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String photo;
    private String password;
    private String username;





    private User user;


    public Profile(
        String photo,        String password,        String username    ) {
        this.photo = photo;
        this.password = password;
        this.username = username;
    }


    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
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