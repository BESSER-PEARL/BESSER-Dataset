





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_CallConversation extends ConversationNode {






    private List<bpmnprof_ParticipantAssociation> bpmnprof_participantassociations;




    private bpmnprof_BPMNCollaboration bpmnprof_bpmncollaboration;


    public bpmnprof_CallConversation(
    ) {
        super(
        );
        this.bpmnprof_participantassociations = new ArrayList<>();
    }

    public bpmnprof_CallConversation(
        ArrayList<bpmnprof_ParticipantAssociation> bpmnprof_participantassociations    ) {
        this.bpmnprof_participantassociations = bpmnprof_participantassociations;
    }


    public List<bpmnprof_ParticipantAssociation> getBpmnprof_participantassociations() {
        return bpmnprof_participantassociations;
    }

    public void addBpmnprof_participantassociation(Bpmnprof_participantassociation bpmnprof_participantassociation) {
        this.bpmnprof_participantassociations.add(bpmnprof_participantassociation);
    }
    public bpmnprof_BPMNCollaboration getBpmnprof_bpmncollaboration() {
        return bpmnprof_bpmncollaboration;
    }

    public void setBpmnprof_bpmncollaboration(bpmnprof_BPMNCollaboration bpmnprof_bpmncollaboration) {
        this.bpmnprof_bpmncollaboration = bpmnprof_bpmncollaboration;
    }

}