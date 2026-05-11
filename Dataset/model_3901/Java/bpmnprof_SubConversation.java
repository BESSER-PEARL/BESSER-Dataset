





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_SubConversation extends ConversationNode {






    private List<bpmnprof_ConversationNode> bpmnprof_conversationnodes;


    public bpmnprof_SubConversation(
    ) {
        super(
        );
        this.bpmnprof_conversationnodes = new ArrayList<>();
    }

    public bpmnprof_SubConversation(
        ArrayList<bpmnprof_ConversationNode> bpmnprof_conversationnodes    ) {
        this.bpmnprof_conversationnodes = bpmnprof_conversationnodes;
    }


    public List<bpmnprof_ConversationNode> getBpmnprof_conversationnodes() {
        return bpmnprof_conversationnodes;
    }

    public void addBpmnprof_conversationnode(Bpmnprof_conversationnode bpmnprof_conversationnode) {
        this.bpmnprof_conversationnodes.add(bpmnprof_conversationnode);
    }

}