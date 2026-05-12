





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String sender;
    private String message;
    private String reciver;





    private User user;


    public Message(
        String sender,        String message,        String reciver    ) {
        this.sender = sender;
        this.message = message;
        this.reciver = reciver;
    }


    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getReciver() {
        return reciver;
    }

    public void setReciver(String reciver) {
        this.reciver = reciver;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}