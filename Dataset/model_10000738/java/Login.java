





import java.util.List;
import java.util.ArrayList;

public class Login  {






    private List<User> users;




    private Database database;


    public Login(
    ) {
        this.users = new ArrayList<>();
    }

    public Login(
        ArrayList<User> users    ) {
        this.users = users;
    }


    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }

}