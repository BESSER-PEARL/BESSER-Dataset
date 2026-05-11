





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ConversationNode extends BaseElement, InteractionNode {

    private String name;





    private BPMN2Model_ConversationAssociation bpmn2model_conversationassociation;




    private List<BPMN2Model_CorrelationKey> bpmn2model_correlationkeys;




    private List<BPMN2Model_MessageFlow> bpmn2model_messageflows;




    private List<BPMN2Model_Participant> bpmn2model_participants;




    private BPMN2Model_SubConversation bpmn2model_subconversation;




    private BPMN2Model_ConversationAssociation bpmn2model_conversationassociation;


    public BPMN2Model_ConversationNode(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_correlationkeys = new ArrayList<>();
        this.bpmn2model_messageflows = new ArrayList<>();
        this.bpmn2model_participants = new ArrayList<>();
    }

    public BPMN2Model_ConversationNode(
        String name        ArrayList<BPMN2Model_CorrelationKey> bpmn2model_correlationkeys,        ArrayList<BPMN2Model_MessageFlow> bpmn2model_messageflows,        ArrayList<BPMN2Model_Participant> bpmn2model_participants    ) {
        this.name = name;
        this.bpmn2model_correlationkeys = bpmn2model_correlationkeys;
        this.bpmn2model_messageflows = bpmn2model_messageflows;
        this.bpmn2model_participants = bpmn2model_participants;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_ConversationAssociation getBpmn2model_conversationassociation() {
        return bpmn2model_conversationassociation;
    }

    public void setBpmn2model_conversationassociation(BPMN2Model_ConversationAssociation bpmn2model_conversationassociation) {
        this.bpmn2model_conversationassociation = bpmn2model_conversationassociation;
    }
    public List<BPMN2Model_CorrelationKey> getBpmn2model_correlationkeys() {
        return bpmn2model_correlationkeys;
    }

    public void addBpmn2model_correlationkey(Bpmn2model_correlationkey bpmn2model_correlationkey) {
        this.bpmn2model_correlationkeys.add(bpmn2model_correlationkey);
    }
    public List<BPMN2Model_MessageFlow> getBpmn2model_messageflows() {
        return bpmn2model_messageflows;
    }

    public void addBpmn2model_messageflow(Bpmn2model_messageflow bpmn2model_messageflow) {
        this.bpmn2model_messageflows.add(bpmn2model_messageflow);
    }
    public List<BPMN2Model_Participant> getBpmn2model_participants() {
        return bpmn2model_participants;
    }

    public void addBpmn2model_participant(Bpmn2model_participant bpmn2model_participant) {
        this.bpmn2model_participants.add(bpmn2model_participant);
    }
    public BPMN2Model_SubConversation getBpmn2model_subconversation() {
        return bpmn2model_subconversation;
    }

    public void setBpmn2model_subconversation(BPMN2Model_SubConversation bpmn2model_subconversation) {
        this.bpmn2model_subconversation = bpmn2model_subconversation;
    }
    public BPMN2Model_ConversationAssociation getBpmn2model_conversationassociation() {
        return bpmn2model_conversationassociation;
    }

    public void setBpmn2model_conversationassociation(BPMN2Model_ConversationAssociation bpmn2model_conversationassociation) {
        this.bpmn2model_conversationassociation = bpmn2model_conversationassociation;
    }

}