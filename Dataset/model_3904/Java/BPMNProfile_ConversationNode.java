





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ConversationNode extends BaseElement, InteractionNode {






    private BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration;




    private List<BPMNProfile_MessageFlow> bpmnprofile_messageflows;


    public BPMNProfile_ConversationNode(
    ) {
        super(
        );
        this.bpmnprofile_messageflows = new ArrayList<>();
    }

    public BPMNProfile_ConversationNode(
        ArrayList<BPMNProfile_MessageFlow> bpmnprofile_messageflows    ) {
        this.bpmnprofile_messageflows = bpmnprofile_messageflows;
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

}