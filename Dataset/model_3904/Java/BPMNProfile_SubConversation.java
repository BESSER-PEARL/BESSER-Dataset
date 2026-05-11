





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SubConversation extends ConversationNode {






    private List<BPMNProfile_ConversationNode> bpmnprofile_conversationnodes;


    public BPMNProfile_SubConversation(
    ) {
        super(
        );
        this.bpmnprofile_conversationnodes = new ArrayList<>();
    }

    public BPMNProfile_SubConversation(
        ArrayList<BPMNProfile_ConversationNode> bpmnprofile_conversationnodes    ) {
        this.bpmnprofile_conversationnodes = bpmnprofile_conversationnodes;
    }


    public List<BPMNProfile_ConversationNode> getBpmnprofile_conversationnodes() {
        return bpmnprofile_conversationnodes;
    }

    public void addBpmnprofile_conversationnode(Bpmnprofile_conversationnode bpmnprofile_conversationnode) {
        this.bpmnprofile_conversationnodes.add(bpmnprofile_conversationnode);
    }

}