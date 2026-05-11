





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ConversationNode extends InteractionNode {






    private bpmnprof_BPMNCollaboration bpmnprof_bpmncollaboration;




    private List<bpmnprof_Participant> bpmnprof_participants;




    private List<bpmnprof_CorrelationKey> bpmnprof_correlationkeys;




    private List<bpmnprof_MessageFlow> bpmnprof_messageflows;


    public bpmnprof_ConversationNode(
    ) {
        super(
        );
        this.bpmnprof_participants = new ArrayList<>();
        this.bpmnprof_correlationkeys = new ArrayList<>();
        this.bpmnprof_messageflows = new ArrayList<>();
    }

    public bpmnprof_ConversationNode(
        ArrayList<bpmnprof_Participant> bpmnprof_participants,        ArrayList<bpmnprof_CorrelationKey> bpmnprof_correlationkeys,        ArrayList<bpmnprof_MessageFlow> bpmnprof_messageflows    ) {
        this.bpmnprof_participants = bpmnprof_participants;
        this.bpmnprof_correlationkeys = bpmnprof_correlationkeys;
        this.bpmnprof_messageflows = bpmnprof_messageflows;
    }


    public bpmnprof_BPMNCollaboration getBpmnprof_bpmncollaboration() {
        return bpmnprof_bpmncollaboration;
    }

    public void setBpmnprof_bpmncollaboration(bpmnprof_BPMNCollaboration bpmnprof_bpmncollaboration) {
        this.bpmnprof_bpmncollaboration = bpmnprof_bpmncollaboration;
    }
    public List<bpmnprof_Participant> getBpmnprof_participants() {
        return bpmnprof_participants;
    }

    public void addBpmnprof_participant(Bpmnprof_participant bpmnprof_participant) {
        this.bpmnprof_participants.add(bpmnprof_participant);
    }
    public List<bpmnprof_CorrelationKey> getBpmnprof_correlationkeys() {
        return bpmnprof_correlationkeys;
    }

    public void addBpmnprof_correlationkey(Bpmnprof_correlationkey bpmnprof_correlationkey) {
        this.bpmnprof_correlationkeys.add(bpmnprof_correlationkey);
    }
    public List<bpmnprof_MessageFlow> getBpmnprof_messageflows() {
        return bpmnprof_messageflows;
    }

    public void addBpmnprof_messageflow(Bpmnprof_messageflow bpmnprof_messageflow) {
        this.bpmnprof_messageflows.add(bpmnprof_messageflow);
    }

}