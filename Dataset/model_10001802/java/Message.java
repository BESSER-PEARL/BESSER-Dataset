





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String maxChars;





    private User user;


    public Message(
        String maxChars    ) {
        this.maxChars = maxChars;
    }


    public String getMaxchars() {
        return maxChars;
    }

    public void setMaxchars(String maxChars) {
        this.maxChars = maxChars;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}