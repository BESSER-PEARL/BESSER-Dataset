





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private String Description;
    private None Name;
    private int RoleID;





    private List<User> users;


    public Role(
        String Description,        None Name,        int RoleID    ) {
        this.Description = Description;
        this.Name = Name;
        this.RoleID = RoleID;
        this.users = new ArrayList<>();
    }

    public Role(
        String Description,        None Name,        int RoleID        ArrayList<User> users    ) {
        this.Description = Description;
        this.Name = Name;
        this.RoleID = RoleID;
        this.users = users;
    }

    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }
    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}