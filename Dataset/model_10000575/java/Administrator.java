





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String admin_name;
    private String password;





    private List<User> users;


    public Administrator(
        String admin_name,        String password    ) {
        this.admin_name = admin_name;
        this.password = password;
        this.users = new ArrayList<>();
    }

    public Administrator(
        String admin_name,        String password        ArrayList<User> users    ) {
        this.admin_name = admin_name;
        this.password = password;
        this.users = users;
    }

    public String getAdmin_name() {
        return admin_name;
    }

    public void setAdmin_name(String admin_name) {
        this.admin_name = admin_name;
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