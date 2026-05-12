





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private String password;
    private String fullname;





    private User user;


    public Registration(
        String userName,        String password,        String fullname    ) {
        this.userName = userName;
        this.password = password;
        this.fullname = fullname;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
        this.fullname = fullname;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}