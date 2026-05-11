





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Participant extends InteractionNode, BaseElement {

    private String name;





    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_ParticipantAssociation bpmn2_participantassociation;




    private bpmn2_ParticipantAssociation bpmn2_participantassociation;


    public bpmn2_Participant(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_ParticipantAssociation getBpmn2_participantassociation() {
        return bpmn2_participantassociation;
    }

    public void setBpmn2_participantassociation(bpmn2_ParticipantAssociation bpmn2_participantassociation) {
        this.bpmn2_participantassociation = bpmn2_participantassociation;
    }
    public bpmn2_ParticipantAssociation getBpmn2_participantassociation() {
        return bpmn2_participantassociation;
    }

    public void setBpmn2_participantassociation(bpmn2_ParticipantAssociation bpmn2_participantassociation) {
        this.bpmn2_participantassociation = bpmn2_participantassociation;
    }

}