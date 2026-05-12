





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private int RoleID;
    private None Name;
    private String Description;





    private List<User> users;


    public Role(
        int RoleID,        None Name,        String Description    ) {
        this.RoleID = RoleID;
        this.Name = Name;
        this.Description = Description;
        this.users = new ArrayList<>();
    }

    public Role(
        int RoleID,        None Name,        String Description        ArrayList<User> users    ) {
        this.RoleID = RoleID;
        this.Name = Name;
        this.Description = Description;
        this.users = users;
    }

    public int getRoleid() {
        return RoleID;
    }

    public void setRoleid(int RoleID) {
        this.RoleID = RoleID;
    }
    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}