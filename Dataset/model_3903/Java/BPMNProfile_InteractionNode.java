





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_InteractionNode  {






    private BPMNProfile_Element bpmnprofile_element;




    private BPMNProfile_MessageFlow bpmnprofile_messageflow;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_ConversationLink bpmnprofile_conversationlink;




    private BPMNProfile_MessageFlow bpmnprofile_messageflow;




    private List<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks;


    public BPMNProfile_InteractionNode(
    ) {
        this.bpmnprofile_conversationlinks = new ArrayList<>();
    }

    public BPMNProfile_InteractionNode(
        ArrayList<BPMNProfile_ConversationLink> bpmnprofile_conversationlinks    ) {
        this.bpmnprofile_conversationlinks = bpmnprofile_conversationlinks;
    }


    public BPMNProfile_Element getBpmnprofile_element() {
        return bpmnprofile_element;
    }

    public void setBpmnprofile_element(BPMNProfile_Element bpmnprofile_element) {
        this.bpmnprofile_element = bpmnprofile_element;
    }
    public BPMNProfile_MessageFlow getBpmnprofile_messageflow() {
        return bpmnprofile_messageflow;
    }

    public void setBpmnprofile_messageflow(BPMNProfile_MessageFlow bpmnprofile_messageflow) {
        this.bpmnprofile_messageflow = bpmnprofile_messageflow;
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
    public List<BPMNProfile_ConversationLink> getBpmnprofile_conversationlinks() {
        return bpmnprofile_conversationlinks;
    }

    public void addBpmnprofile_conversationlink(Bpmnprofile_conversationlink bpmnprofile_conversationlink) {
        this.bpmnprofile_conversationlinks.add(bpmnprofile_conversationlink);
    }

}