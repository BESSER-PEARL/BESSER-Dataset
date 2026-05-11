





import java.util.List;
import java.util.ArrayList;

public class behaviour_SendMessage extends Instruction {

    private String messageType;



    public behaviour_SendMessage(
        String messageType    ) {
        super(
        );
        this.messageType = messageType;
    }


    public String getMessagetype() {
        return messageType;
    }

    public void setMessagetype(String messageType) {
        this.messageType = messageType;
    }


}