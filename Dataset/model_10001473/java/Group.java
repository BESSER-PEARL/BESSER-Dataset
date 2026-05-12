





import java.util.List;
import java.util.ArrayList;

public class Group  {






    private List<User> users;


    public Group(
    ) {
        this.users = new ArrayList<>();
    }

    public Group(
        ArrayList<User> users    ) {
        this.users = users;
    }


    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}