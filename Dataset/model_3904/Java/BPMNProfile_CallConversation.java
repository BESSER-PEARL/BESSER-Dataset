





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CallConversation extends ConversationNode {






    private List<BPMNProfile_ParticipantAssociation> bpmnprofile_participantassociations;




    private BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration;


    public BPMNProfile_CallConversation(
    ) {
        super(
        );
        this.bpmnprofile_participantassociations = new ArrayList<>();
    }

    public BPMNProfile_CallConversation(
        ArrayList<BPMNProfile_ParticipantAssociation> bpmnprofile_participantassociations    ) {
        this.bpmnprofile_participantassociations = bpmnprofile_participantassociations;
    }


    public List<BPMNProfile_ParticipantAssociation> getBpmnprofile_participantassociations() {
        return bpmnprofile_participantassociations;
    }

    public void addBpmnprofile_participantassociation(Bpmnprofile_participantassociation bpmnprofile_participantassociation) {
        this.bpmnprofile_participantassociations.add(bpmnprofile_participantassociation);
    }
    public BPMNProfile_BPMNCollaboration getBpmnprofile_bpmncollaboration() {
        return bpmnprofile_bpmncollaboration;
    }

    public void setBpmnprofile_bpmncollaboration(BPMNProfile_BPMNCollaboration bpmnprofile_bpmncollaboration) {
        this.bpmnprofile_bpmncollaboration = bpmnprofile_bpmncollaboration;
    }

}