





import java.util.List;
import java.util.ArrayList;

public class Login  {






    private Database database;




    private List<User> users;


    public Login(
    ) {
        this.users = new ArrayList<>();
    }

    public Login(
        ArrayList<User> users    ) {
        this.users = users;
    }


    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }
    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}