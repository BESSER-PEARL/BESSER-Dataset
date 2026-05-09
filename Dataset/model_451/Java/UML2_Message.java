





import java.util.List;
import java.util.ArrayList;

public class UML2_Message extends NamedElement {

    private String messageSort;
    private String messageKind;



    public UML2_Message(
        String messageSort,        String messageKind    ) {
        super(
        );
        this.messageSort = messageSort;
        this.messageKind = messageKind;
    }


    public String getMessagesort() {
        return messageSort;
    }

    public void setMessagesort(String messageSort) {
        this.messageSort = messageSort;
    }
    public String getMessagekind() {
        return messageKind;
    }

    public void setMessagekind(String messageKind) {
        this.messageKind = messageKind;
    }


}