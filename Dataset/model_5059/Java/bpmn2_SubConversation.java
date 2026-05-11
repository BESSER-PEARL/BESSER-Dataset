





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubConversation extends ConversationNode {






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


    public List<bpmn2_ConversationNode> getBpmn2_conversationnodes() {
        return bpmn2_conversationnodes;
    }

    public void addBpmn2_conversationnode(Bpmn2_conversationnode bpmn2_conversationnode) {
        this.bpmn2_conversationnodes.add(bpmn2_conversationnode);
    }

}