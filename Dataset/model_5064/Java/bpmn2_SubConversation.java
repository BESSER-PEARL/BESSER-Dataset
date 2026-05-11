





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubConversation extends ConversationNode {






    private bpmn2_DocumentRoot bpmn2_documentroot;




    private List<bpmn2_ConversationNode> bpmn2_conversationnodes;


    public bpmn2_SubConversation(
    ) {
        super(
        );
        this.bpmn2_conversationnodes = new ArrayList<>();
    }

    public bpmn2_SubConversation(
        ArrayList<bpmn2_ConversationNode> bpmn2_conversationnodes    ) {
        this.bpmn2_conversationnodes = bpmn2_conversationnodes;
    }


    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public List<bpmn2_ConversationNode> getBpmn2_conversationnodes() {
        return bpmn2_conversationnodes;
    }

    public void addBpmn2_conversationnode(Bpmn2_conversationnode bpmn2_conversationnode) {
        this.bpmn2_conversationnodes.add(bpmn2_conversationnode);
    }

}