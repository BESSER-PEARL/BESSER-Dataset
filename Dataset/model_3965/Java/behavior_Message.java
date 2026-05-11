





import java.util.List;
import java.util.ArrayList;

public class behavior_Message extends NamedElement {

    private int MessageOrder;





    private behavior_Connector behavior_connector;




    private behavior_MessageEnd behavior_messageend;




    private behavior_MessageEnd behavior_messageend;




    private behavior_MessageEnd behavior_messageend;


    public behavior_Message(
        int MessageOrder    ) {
        super(
        );
        this.MessageOrder = MessageOrder;
    }


    public int getMessageorder() {
        return MessageOrder;
    }

    public void setMessageorder(int MessageOrder) {
        this.MessageOrder = MessageOrder;
    }

    public behavior_Connector getBehavior_connector() {
        return behavior_connector;
    }

    public void setBehavior_connector(behavior_Connector behavior_connector) {
        this.behavior_connector = behavior_connector;
    }
    public behavior_MessageEnd getBehavior_messageend() {
        return behavior_messageend;
    }

    public void setBehavior_messageend(behavior_MessageEnd behavior_messageend) {
        this.behavior_messageend = behavior_messageend;
    }
    public behavior_MessageEnd getBehavior_messageend() {
        return behavior_messageend;
    }

    public void setBehavior_messageend(behavior_MessageEnd behavior_messageend) {
        this.behavior_messageend = behavior_messageend;
    }
    public behavior_MessageEnd getBehavior_messageend() {
        return behavior_messageend;
    }

    public void setBehavior_messageend(behavior_MessageEnd behavior_messageend) {
        this.behavior_messageend = behavior_messageend;
    }

}