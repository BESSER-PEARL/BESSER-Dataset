





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String reciver;
    private String message;
    private String sender;





    private User user;


    public Message(
        String reciver,        String message,        String sender    ) {
        this.reciver = reciver;
        this.message = message;
        this.sender = sender;
    }


    public String getReciver() {
        return reciver;
    }

    public void setReciver(String reciver) {
        this.reciver = reciver;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}