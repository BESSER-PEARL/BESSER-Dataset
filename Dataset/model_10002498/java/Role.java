





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private int RoleID;
    private String Description;
    private None Name;





    private List<User> users;


    public Role(
        int RoleID,        String Description,        None Name    ) {
        this.RoleID = RoleID;
        this.Description = Description;
        this.Name = Name;
        this.users = new ArrayList<>();
    }

    public Role(
        int RoleID,        String Description,        None Name        ArrayList<User> users    ) {
        this.RoleID = RoleID;
        this.Description = Description;
        this.Name = Name;
        this.users = users;
    }

    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
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

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}