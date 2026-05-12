





import java.util.List;
import java.util.ArrayList;

public class User  {






    private Login login;




    private List<Message> messages;


    public User(
    ) {
        this.messages = new ArrayList<>();
    }

    public User(
        ArrayList<Message> messages    ) {
        this.messages = messages;
    }


    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
    }

}