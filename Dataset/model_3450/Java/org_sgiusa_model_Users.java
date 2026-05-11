





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Users  {






    private List<User> users;


    public org_sgiusa_model_Users(
    ) {
        this.users = new ArrayList<>();
    }

    public org_sgiusa_model_Users(
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