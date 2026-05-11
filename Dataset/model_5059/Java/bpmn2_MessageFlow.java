





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MessageFlow extends BaseElement {

    private String name;





    private bpmn2_MessageFlowAssociation bpmn2_messageflowassociation;




    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_InteractionNode bpmn2_interactionnode;




    private bpmn2_Message bpmn2_message;




    private bpmn2_InteractionNode bpmn2_interactionnode;




    private bpmn2_MessageFlowAssociation bpmn2_messageflowassociation;




    private bpmn2_ConversationNode bpmn2_conversationnode;


    public bpmn2_MessageFlow(
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

    public bpmn2_MessageFlowAssociation getBpmn2_messageflowassociation() {
        return bpmn2_messageflowassociation;
    }

    public void setBpmn2_messageflowassociation(bpmn2_MessageFlowAssociation bpmn2_messageflowassociation) {
        this.bpmn2_messageflowassociation = bpmn2_messageflowassociation;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public bpmn2_InteractionNode getBpmn2_interactionnode() {
        return bpmn2_interactionnode;
    }

    public void setBpmn2_interactionnode(bpmn2_InteractionNode bpmn2_interactionnode) {
        this.bpmn2_interactionnode = bpmn2_interactionnode;
    }
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_InteractionNode getBpmn2_interactionnode() {
        return bpmn2_interactionnode;
    }

    public void setBpmn2_interactionnode(bpmn2_InteractionNode bpmn2_interactionnode) {
        this.bpmn2_interactionnode = bpmn2_interactionnode;
    }
    public bpmn2_MessageFlowAssociation getBpmn2_messageflowassociation() {
        return bpmn2_messageflowassociation;
    }

    public void setBpmn2_messageflowassociation(bpmn2_MessageFlowAssociation bpmn2_messageflowassociation) {
        this.bpmn2_messageflowassociation = bpmn2_messageflowassociation;
    }
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }

}