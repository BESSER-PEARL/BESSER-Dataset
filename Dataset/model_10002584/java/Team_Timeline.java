





import java.util.List;
import java.util.ArrayList;

public class Team_Timeline  {

    private String Name;





    private User user;


    public Team_Timeline(
        String Name    ) {
        this.Name = Name;
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