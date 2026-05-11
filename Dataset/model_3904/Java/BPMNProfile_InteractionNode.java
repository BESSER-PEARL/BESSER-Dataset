





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_InteractionNode  {






    private List<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_MessageFlow bpmnprofile_messageflow;




    private BPMNProfile_MessageFlow bpmnprofile_messageflow;


    public BPMNProfile_InteractionNode(
    ) {
        this.bpmnprofile_conversationlinks = new ArrayList<>();
    }

    public BPMNProfile_InteractionNode(
        ArrayList<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks    ) {
        this.bpmnprofile_conversationlinks = bpmnprofile_conversationlinks;
    }


    public List<BPMNProfile_ConversationLink> getBpmnprofile_conversationlinks() {
        return bpmnprofile_conversationlinks;
    }

    public void addBpmnprofile_conversationlink(Bpmnprofile_conversationlink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlinks.add(bpmnprofile_conversationlink);
    }
    public BPMNProfile_ConversationLink getBpmnprofile_conversationlink() {
        return bpmnprofile_conversationlink;
    }

    public void setBpmnprofile_conversationlink(BPMNProfile_ConversationLink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlink = bpmnprofile_conversationlink;
    }
    public BPMNProfile_ConversationLink getBpmnprofile_conversationlink() {
        return bpmnprofile_conversationlink;
    }

    public void setBpmnprofile_conversationlink(BPMNProfile_ConversationLink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlink = bpmnprofile_conversationlink;
    }
    public BPMNProfile_ConversationLink getBpmnprofile_conversationlink() {
        return bpmnprofile_conversationlink;
    }

    public void setBpmnprofile_conversationlink(BPMNProfile_ConversationLink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlink = bpmnprofile_conversationlink;
    }
    public BPMNProfile_MessageFlow getBpmnprofile_messageflow() {
        return bpmnprofile_messageflow;
    }

    public void setBpmnprofile_messageflow(BPMNProfile_MessageFlow bpmnprofile_messageflow) {
        this.bpmnprofile_messageflow = bpmnprofile_messageflow;
    }
    public BPMNProfile_MessageFlow getBpmnprofile_messageflow() {
        return bpmnprofile_messageflow;
    }

    public void setBpmnprofile_messageflow(BPMNProfile_MessageFlow bpmnprofile_messageflow) {
        this.bpmnprofile_messageflow = bpmnprofile_messageflow;
    }

}