





import java.util.List;
import java.util.ArrayList;

public class behavior_Message extends NamedElement {

    private int MessageOrder;





    private behavior_Connector behavior_connector;


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

}