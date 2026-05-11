





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_UserGroup  {

    private String name;





    private List<User> users;


    public camel_organisation_UserGroup(
        String name    ) {
        this.name = name;
        this.users = new ArrayList<>();
    }

    public camel_organisation_UserGroup(
        String name        ArrayList<User> users    ) {
        this.name = name;
        this.users = users;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}