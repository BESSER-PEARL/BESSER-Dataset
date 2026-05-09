





import java.util.List;
import java.util.ArrayList;

public class HALL_Messages_NamedMessageState extends MessageState {

    private String name;





    private MessageHandler messagehandler;


    public HALL_Messages_NamedMessageState(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MessageHandler getMessagehandler() {
        return messagehandler;
    }

    public void setMessagehandler(MessageHandler messagehandler) {
        this.messagehandler = messagehandler;
    }

}