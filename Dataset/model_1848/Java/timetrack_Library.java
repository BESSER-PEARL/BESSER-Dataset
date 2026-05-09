





import java.util.List;
import java.util.ArrayList;

public class timetrack_Library  {






    private List<timetrack_User> timetrack_users;


    public timetrack_Library(
    ) {
        this.timetrack_users = new ArrayList<>();
    }

    public timetrack_Library(
        ArrayList<timetrack_User> timetrack_users    ) {
        this.timetrack_users = timetrack_users;
    }


    public List<timetrack_User> getTimetrack_users() {
        return timetrack_users;
    }

    public void addTimetrack_user(Timetrack_user timetrack_user) {
        this.timetrack_users.add(timetrack_user);
    }

}