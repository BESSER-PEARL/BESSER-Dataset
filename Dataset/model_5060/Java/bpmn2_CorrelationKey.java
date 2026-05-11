





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CorrelationKey extends BaseElement {

    private String name;





    private List<bpmn2_CorrelationProperty> bpmn2_correlationpropertys;




    private bpmn2_CorrelationSubscription bpmn2_correlationsubscription;




    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_ChoreographyActivity bpmn2_choreographyactivity;


    public bpmn2_CorrelationKey(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_correlationpropertys = new ArrayList<>();
    }

    public bpmn2_CorrelationKey(
        String name        ArrayList<bpmn2_CorrelationProperty> bpmn2_correlationpropertys    ) {
        this.name = name;
        this.bpmn2_correlationpropertys = bpmn2_correlationpropertys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_CorrelationProperty> getBpmn2_correlationpropertys() {
        return bpmn2_correlationpropertys;
    }

    public void addBpmn2_correlationproperty(Bpmn2_correlationproperty bpmn2_correlationproperty) {
        this.bpmn2_correlationpropertys.add(bpmn2_correlationproperty);
    }
    public bpmn2_CorrelationSubscription getBpmn2_correlationsubscription() {
        return bpmn2_correlationsubscription;
    }

    public void setBpmn2_correlationsubscription(bpmn2_CorrelationSubscription bpmn2_correlationsubscription) {
        this.bpmn2_correlationsubscription = bpmn2_correlationsubscription;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_ChoreographyActivity getBpmn2_choreographyactivity() {
        return bpmn2_choreographyactivity;
    }

    public void setBpmn2_choreographyactivity(bpmn2_ChoreographyActivity bpmn2_choreographyactivity) {
        this.bpmn2_choreographyactivity = bpmn2_choreographyactivity;
    }

}