





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ConversationNode extends InteractionNode {






    private BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration;




    private List<BPMNProfile_MessageFlow> bpmnprofile_messageflows;




    private List<BPMNProfile_Participant> bpmnprofile_participants;




    private List<BPMNProfile_CorrelationKey> bpmnprofile_correlationkeys;




    private BPMNProfile_SubConversation bpmnprofile_subconversation;


    public BPMNProfile_ConversationNode(
    ) {
        super(
        );
        this.bpmnprofile_messageflows = new ArrayList<>();
        this.bpmnprofile_participants = new ArrayList<>();
        this.bpmnprofile_correlationkeys = new ArrayList<>();
    }

    public BPMNProfile_ConversationNode(
        ArrayList<BPMNProfile_MessageFlow> bpmnprofile_messageflows,        ArrayList<BPMNProfile_Participant> bpmnprofile_participants,        ArrayList<BPMNProfile_CorrelationKey> bpmnprofile_correlationkeys    ) {
        this.bpmnprofile_messageflows = bpmnprofile_messageflows;
        this.bpmnprofile_participants = bpmnprofile_participants;
        this.bpmnprofile_correlationkeys = bpmnprofile_correlationkeys;
    }


    public BPMNProfile_BPMNCollaboration getBpmnprofile_bpmncollaboration() {
        return bpmnprofile_bpmncollaboration;
    }

    public void setBpmnprofile_bpmncollaboration(BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration) {
        this.bpmnprofile_bpmncollaboration = bpmnprofile_bpmncollaboration;
    }
    public List<BPMNProfile_MessageFlow> getBpmnprofile_messageflows() {
        return bpmnprofile_messageflows;
    }

    public void addBpmnprofile_messageflow(Bpmnprofile_messageflow bpmnprofile_messageflow) {
        this.bpmnprofile_messageflows.add(bpmnprofile_messageflow);
    }
    public List<BPMNProfile_Participant> getBpmnprofile_participants() {
        return bpmnprofile_participants;
    }

    public void addBpmnprofile_participant(Bpmnprofile_participant bpmnprofile_participant) {
        this.bpmnprofile_participants.add(bpmnprofile_participant);
    }
    public List<BPMNProfile_CorrelationKey> getBpmnprofile_correlationkeys() {
        return bpmnprofile_correlationkeys;
    }

    public void addBpmnprofile_correlationkey(Bpmnprofile_correlationkey bpmnprofile_correlationkey) {
        this.bpmnprofile_correlationkeys.add(bpmnprofile_correlationkey);
    }
    public BPMNProfile_SubConversation getBpmnprofile_subconversation() {
        return bpmnprofile_subconversation;
    }

    public void setBpmnprofile_subconversation(BPMNProfile_SubConversation bpmnprofile_subconversation) {
        this.bpmnprofile_subconversation = bpmnprofile_subconversation;
    }

}