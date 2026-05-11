





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MessageFlow extends BaseElement {

    private String name;





    private bpmn2_MessageFlowAssociation bpmn2_messageflowassociation;




    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_MessageFlowAssociation bpmn2_messageflowassociation;


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
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_MessageFlowAssociation getBpmn2_messageflowassociation() {
        return bpmn2_messageflowassociation;
    }

    public void setBpmn2_messageflowassociation(bpmn2_MessageFlowAssociation bpmn2_messageflowassociation) {
        this.bpmn2_messageflowassociation = bpmn2_messageflowassociation;
    }

}