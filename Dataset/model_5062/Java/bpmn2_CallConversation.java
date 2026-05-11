





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CallConversation extends ConversationNode {






    private bpmn2_Collaboration bpmn2_collaboration;




    private List<bpmn2_ParticipantAssociation> bpmn2_participantassociations;


    public bpmn2_CallConversation(
    ) {
        super(
        );
        this.bpmn2_participantassociations = new ArrayList<>();
    }

    public bpmn2_CallConversation(
        ArrayList<bpmn2_ParticipantAssociation> bpmn2_participantassociations    ) {
        this.bpmn2_participantassociations = bpmn2_participantassociations;
    }


    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public List<bpmn2_ParticipantAssociation> getBpmn2_participantassociations() {
        return bpmn2_participantassociations;
    }

    public void addBpmn2_participantassociation(Bpmn2_participantassociation bpmn2_participantassociation) {
        this.bpmn2_participantassociations.add(bpmn2_participantassociation);
    }

}