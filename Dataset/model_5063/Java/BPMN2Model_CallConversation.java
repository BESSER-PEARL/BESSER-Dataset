





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CallConversation extends ConversationNode {






    private List<BPMN2Model_ParticipantAssociation> bpmn2model_participantassociations;


    public BPMN2Model_CallConversation(
    ) {
        super(
        );
        this.bpmn2model_participantassociations = new ArrayList<>();
    }

    public BPMN2Model_CallConversation(
        ArrayList<BPMN2Model_ParticipantAssociation> bpmn2model_participantassociations    ) {
        this.bpmn2model_participantassociations = bpmn2model_participantassociations;
    }


    public List<BPMN2Model_ParticipantAssociation> getBpmn2model_participantassociations() {
        return bpmn2model_participantassociations;
    }

    public void addBpmn2model_participantassociation(Bpmn2model_participantassociation bpmn2model_participantassociation) {
        this.bpmn2model_participantassociations.add(bpmn2model_participantassociation);
    }

}