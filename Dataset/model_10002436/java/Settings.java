





import java.util.List;
import java.util.ArrayList;

public class Settings  {

    private String firstName;
    private String notificationChannels;
    private String email;
    private String name;
    private String username;





    private User user;




    private User user;


    public Settings(
        String firstName,        String notificationChannels,        String email,        String name,        String username    ) {
        this.firstName = firstName;
        this.notificationChannels = notificationChannels;
        this.email = email;
        this.name = name;
        this.username = username;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getNotificationchannels() {
        return notificationChannels;
    }

    public void setNotificationchannels(String notificationChannels) {
        this.notificationChannels = notificationChannels;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}