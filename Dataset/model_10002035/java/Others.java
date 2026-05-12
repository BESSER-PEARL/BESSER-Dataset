





import java.util.List;
import java.util.ArrayList;

public class Others  {

    private String discription;
    private String name;





    private User user;


    public Others(
        String discription,        String name    ) {
        this.discription = discription;
        this.name = name;
    }


    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}