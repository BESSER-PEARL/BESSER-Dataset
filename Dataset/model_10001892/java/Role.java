





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private String type;





    private List<User> users;


    public Role(
        String type    ) {
        this.type = type;
        this.users = new ArrayList<>();
    }

    public Role(
        String type        ArrayList<User> users    ) {
        this.type = type;
        this.users = users;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}