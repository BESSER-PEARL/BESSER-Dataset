





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String Description;
    private String Name;





    private User user;


    public Group(
        String Description,        String Name    ) {
        this.Description = Description;
        this.Name = Name;
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

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}