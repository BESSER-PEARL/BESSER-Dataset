





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String userName;
    private String password;
    private String name;
    private String username;





    private User user;


    public Registration(
        String userName,        String password,        String name,        String username    ) {
        this.userName = userName;
        this.password = password;
        this.name = name;
        this.username = username;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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