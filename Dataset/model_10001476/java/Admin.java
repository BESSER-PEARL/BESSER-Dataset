





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String username;
    private String password;





    private Event event;


    public Admin(
        String username,        String password    ) {
        this.username = username;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Event getEvent() {
        return event;
    }

    public void setEvent(Event event) {
        this.event = event;
    }

}