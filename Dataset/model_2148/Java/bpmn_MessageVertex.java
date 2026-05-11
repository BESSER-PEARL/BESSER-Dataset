





import java.util.List;
import java.util.ArrayList;

public class bpmn_MessageVertex extends NamedBpmnObject, Identifiable {

    private String orderedMessages;



    public bpmn_MessageVertex(
        String orderedMessages    ) {
        super(
        );
        this.orderedMessages = orderedMessages;
    }


    public String getOrderedmessages() {
        return orderedMessages;
    }

    public void setOrderedmessages(String orderedMessages) {
        this.orderedMessages = orderedMessages;
    }


}