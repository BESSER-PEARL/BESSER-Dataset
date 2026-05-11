





import java.util.List;
import java.util.ArrayList;

public class bpmn2_InteractionNode  {






    private bpmn2_MessageFlow bpmn2_messageflow;




    private List<bpmn2_ConversationLink> bpmn2_conversationlinks;




    private bpmn2_MessageFlow bpmn2_messageflow;




    private bpmn2_ConversationLink bpmn2_conversationlink;




    private List<bpmn2_ConversationLink> bpmn2_conversationlinks;




    private bpmn2_ConversationLink bpmn2_conversationlink;


    public bpmn2_InteractionNode(
    ) {
        this.bpmn2_conversationlinks = new ArrayList<>();
        this.bpmn2_conversationlinks = new ArrayList<>();
    }

    public bpmn2_InteractionNode(
        ArrayList<bpmn2_ConversationLink> bpmn2_conversationlinks,        ArrayList<bpmn2_ConversationLink> bpmn2_conversationlinks    ) {
        this.bpmn2_conversationlinks = bpmn2_conversationlinks;
        this.bpmn2_conversationlinks = bpmn2_conversationlinks;
    }


    public bpmn2_MessageFlow getBpmn2_messageflow() {
        return bpmn2_messageflow;
    }

    public void setBpmn2_messageflow(bpmn2_MessageFlow bpmn2_messageflow) {
        this.bpmn2_messageflow = bpmn2_messageflow;
    }
    public List<bpmn2_ConversationLink> getBpmn2_conversationlinks() {
        return bpmn2_conversationlinks;
    }

    public void addBpmn2_conversationlink(Bpmn2_conversationlink bpmn2_conversationlink) {
        this.bpmn2_conversationlinks.add(bpmn2_conversationlink);
    }
    public bpmn2_MessageFlow getBpmn2_messageflow() {
        return bpmn2_messageflow;
    }

    public void setBpmn2_messageflow(bpmn2_MessageFlow bpmn2_messageflow) {
        this.bpmn2_messageflow = bpmn2_messageflow;
    }
    public bpmn2_ConversationLink getBpmn2_conversationlink() {
        return bpmn2_conversationlink;
    }

    public void setBpmn2_conversationlink(bpmn2_ConversationLink bpmn2_conversationlink) {
        this.bpmn2_conversationlink = bpmn2_conversationlink;
    }
    public List<bpmn2_ConversationLink> getBpmn2_conversationlinks() {
        return bpmn2_conversationlinks;
    }

    public void addBpmn2_conversationlink(Bpmn2_conversationlink bpmn2_conversationlink) {
        this.bpmn2_conversationlinks.add(bpmn2_conversationlink);
    }
    public bpmn2_ConversationLink getBpmn2_conversationlink() {
        return bpmn2_conversationlink;
    }

    public void setBpmn2_conversationlink(bpmn2_ConversationLink bpmn2_conversationlink) {
        this.bpmn2_conversationlink = bpmn2_conversationlink;
    }

}