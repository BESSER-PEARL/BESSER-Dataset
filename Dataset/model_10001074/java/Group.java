





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String name;
    private String discription;





    private User user;


    public Group(
        String name,        String discription    ) {
        this.name = name;
        this.discription = discription;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}