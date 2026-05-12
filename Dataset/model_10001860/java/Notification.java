





import java.util.List;
import java.util.ArrayList;

public class Notification  {

    private String update;





    private User user;


    public Notification(
        String update    ) {
        this.update = update;
    }


    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}