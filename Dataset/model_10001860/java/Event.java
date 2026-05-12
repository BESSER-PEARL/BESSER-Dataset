





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private String name;
    private String time;
    private String location;





    private User user;


    public Event(
        String name,        String time,        String location    ) {
        this.name = name;
        this.time = time;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}