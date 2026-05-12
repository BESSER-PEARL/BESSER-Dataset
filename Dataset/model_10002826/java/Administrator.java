





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String password;
    private String admin_name;





    private List<User> users;


    public Administrator(
        String password,        String admin_name    ) {
        this.password = password;
        this.admin_name = admin_name;
        this.users = new ArrayList<>();
    }

    public Administrator(
        String password,        String admin_name        ArrayList<User> users    ) {
        this.password = password;
        this.admin_name = admin_name;
        this.users = users;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getAdmin_name() {
        return admin_name;
    }

    public void setAdmin_name(String admin_name) {
        this.admin_name = admin_name;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}