





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String Description;
    private String Name;
    private int ID_User;
    private int ID_Group;





    private User user;


    public Group(
        String Description,        String Name,        int ID_User,        int ID_Group    ) {
        this.Description = Description;
        this.Name = Name;
        this.ID_User = ID_User;
        this.ID_Group = ID_Group;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId_user() {
        return ID_User;
    }

    public void setId_user(int ID_User) {
        this.ID_User = ID_User;
    }
    public int getId_group() {
        return ID_Group;
    }

    public void setId_group(int ID_Group) {
        this.ID_Group = ID_Group;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}