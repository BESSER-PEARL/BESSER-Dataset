





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ConversationNode extends BaseElement, InteractionNode {

    private String name;





    private bpmn2_ConversationAssociation bpmn2_conversationassociation;




    private bpmn2_ConversationAssociation bpmn2_conversationassociation;




    private bpmn2_Collaboration bpmn2_collaboration;




    private List<bpmn2_Participant> bpmn2_participants;




    private List<bpmn2_CorrelationKey> bpmn2_correlationkeys;


    public bpmn2_ConversationNode(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_participants = new ArrayList<>();
        this.bpmn2_correlationkeys = new ArrayList<>();
    }

    public bpmn2_ConversationNode(
        String name        ArrayList<bpmn2_Participant> bpmn2_participants,        ArrayList<bpmn2_CorrelationKey> bpmn2_correlationkeys    ) {
        this.name = name;
        this.bpmn2_participants = bpmn2_participants;
        this.bpmn2_correlationkeys = bpmn2_correlationkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ConversationAssociation getBpmn2_conversationassociation() {
        return bpmn2_conversationassociation;
    }

    public void setBpmn2_conversationassociation(bpmn2_ConversationAssociation bpmn2_conversationassociation) {
        this.bpmn2_conversationassociation = bpmn2_conversationassociation;
    }
    public bpmn2_ConversationAssociation getBpmn2_conversationassociation() {
        return bpmn2_conversationassociation;
    }

    public void setBpmn2_conversationassociation(bpmn2_ConversationAssociation bpmn2_conversationassociation) {
        this.bpmn2_conversationassociation = bpmn2_conversationassociation;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }
    public List<bpmn2_CorrelationKey> getBpmn2_correlationkeys() {
        return bpmn2_correlationkeys;
    }

    public void addBpmn2_correlationkey(Bpmn2_correlationkey bpmn2_correlationkey) {
        this.bpmn2_correlationkeys.add(bpmn2_correlationkey);
    }

}