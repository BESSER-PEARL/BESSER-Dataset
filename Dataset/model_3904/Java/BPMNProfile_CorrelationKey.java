





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CorrelationKey extends BaseElement {






    private BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration;




    private BPMNProfile_ConversationNode bpmnprofile_conversationnode;




    private BPMNProfile_CorrelationSubscription bpmnprofile_correlationsubscription;


    public BPMNProfile_CorrelationKey(
    ) {
        super(
        );
    }



    public BPMNProfile_BPMNCollaboration getBpmnprofile_bpmncollaboration() {
        return bpmnprofile_bpmncollaboration;
    }

    public void setBpmnprofile_bpmncollaboration(BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration) {
        this.bpmnprofile_bpmncollaboration = bpmnprofile_bpmncollaboration;
    }
    public BPMNProfile_ConversationNode getBpmnprofile_conversationnode() {
        return bpmnprofile_conversationnode;
    }

    public void setBpmnprofile_conversationnode(BPMNProfile_ConversationNode bpmnprofile_conversationnode) {
        this.bpmnprofile_conversationnode = bpmnprofile_conversationnode;
    }
    public BPMNProfile_CorrelationSubscription getBpmnprofile_correlationsubscription() {
        return bpmnprofile_correlationsubscription;
    }

    public void setBpmnprofile_correlationsubscription(BPMNProfile_CorrelationSubscription bpmnprofile_correlationsubscription) {
        this.bpmnprofile_correlationsubscription = bpmnprofile_correlationsubscription;
    }

}