





import java.util.List;
import java.util.ArrayList;

public class farmbot_modeling_SendMessage extends SequenceCommand {

    private String message;
    private String messageType;



    public farmbot_modeling_SendMessage(
        String message,        String messageType    ) {
        super(
        );
        this.message = message;
        this.messageType = messageType;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getMessagetype() {
        return messageType;
    }

    public void setMessagetype(String messageType) {
        this.messageType = messageType;
    }


}