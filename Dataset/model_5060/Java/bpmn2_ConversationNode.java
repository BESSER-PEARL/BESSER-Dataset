





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ConversationNode extends BaseElement, InteractionNode {

    private String name;





    private List<bpmn2_Participant> bpmn2_participants;




    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_ConversationAssociation bpmn2_conversationassociation;




    private List<bpmn2_MessageFlow> bpmn2_messageflows;




    private bpmn2_SubConversation bpmn2_subconversation;




    private bpmn2_ConversationAssociation bpmn2_conversationassociation;


    public bpmn2_ConversationNode(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_participants = new ArrayList<>();
        this.bpmn2_messageflows = new ArrayList<>();
    }

    public bpmn2_ConversationNode(
        String name        ArrayList<bpmn2_Participant> bpmn2_participants,        ArrayList<bpmn2_MessageFlow> bpmn2_messageflows    ) {
        this.name = name;
        this.bpmn2_participants = bpmn2_participants;
        this.bpmn2_messageflows = bpmn2_messageflows;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_Participant> getBpmn2_participants() {
        return bpmn2_participants;
    }

    public void addBpmn2_participant(Bpmn2_participant bpmn2_participant) {
        this.bpmn2_participants.add(bpmn2_participant);
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public bpmn2_ConversationAssociation getBpmn2_conversationassociation() {
        return bpmn2_conversationassociation;
    }

    public void setBpmn2_conversationassociation(bpmn2_ConversationAssociation bpmn2_conversationassociation) {
        this.bpmn2_conversationassociation = bpmn2_conversationassociation;
    }
    public List<bpmn2_MessageFlow> getBpmn2_messageflows() {
        return bpmn2_messageflows;
    }

    public void addBpmn2_messageflow(Bpmn2_messageflow bpmn2_messageflow) {
        this.bpmn2_messageflows.add(bpmn2_messageflow);
    }
    public bpmn2_SubConversation getBpmn2_subconversation() {
        return bpmn2_subconversation;
    }

    public void setBpmn2_subconversation(bpmn2_SubConversation bpmn2_subconversation) {
        this.bpmn2_subconversation = bpmn2_subconversation;
    }
    public bpmn2_ConversationAssociation getBpmn2_conversationassociation() {
        return bpmn2_conversationassociation;
    }

    public void setBpmn2_conversationassociation(bpmn2_ConversationAssociation bpmn2_conversationassociation) {
        this.bpmn2_conversationassociation = bpmn2_conversationassociation;
    }

}