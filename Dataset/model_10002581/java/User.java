





import java.util.List;
import java.util.ArrayList;

public class User  {






    private List<Message> messages;




    private Login login;


    public User(
    ) {
        this.messages = new ArrayList<>();
    }

    public User(
        ArrayList<Message> messages    ) {
        this.messages = messages;
    }


    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
    }
    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}