





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private String userName;
    private String password;





    private List<User> users;


    public User(
        String email,        String userName,        String password    ) {
        this.email = email;
        this.userName = userName;
        this.password = password;
        this.users = new ArrayList<>();
    }

    public User(
        String email,        String userName,        String password        ArrayList<User> users    ) {
        this.email = email;
        this.userName = userName;
        this.password = password;
        this.users = users;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}