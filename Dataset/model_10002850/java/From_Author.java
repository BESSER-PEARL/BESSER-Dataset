





import java.util.List;
import java.util.ArrayList;

public class From_Author  {






    private List<message> messages;


    public From_Author(
    ) {
        this.messages = new ArrayList<>();
    }

    public From_Author(
        ArrayList<message> messages    ) {
        this.messages = messages;
    }


    public List<message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
    }

}