





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_InteractionNode extends BPMNBase {






    private List<BPMN2Model_ConversationLink> bpmn2model_conversationlinks;




    private BPMN2Model_ConversationLink bpmn2model_conversationlink;




    private BPMN2Model_MessageFlow bpmn2model_messageflow;




    private BPMN2Model_ConversationLink bpmn2model_conversationlink;




    private BPMN2Model_MessageFlow bpmn2model_messageflow;




    private List<BPMN2Model_ConversationLink> bpmn2model_conversationlinks;


    public BPMN2Model_InteractionNode(
    ) {
        super(
        );
        this.bpmn2model_conversationlinks = new ArrayList<>();
        this.bpmn2model_conversationlinks = new ArrayList<>();
    }

    public BPMN2Model_InteractionNode(
        ArrayList<BPMN2Model_ConversationLink> bpmn2model_conversationlinks,        ArrayList<BPMN2Model_ConversationLink> bpmn2model_conversationlinks    ) {
        this.bpmn2model_conversationlinks = bpmn2model_conversationlinks;
        this.bpmn2model_conversationlinks = bpmn2model_conversationlinks;
    }


    public List<BPMN2Model_ConversationLink> getBpmn2model_conversationlinks() {
        return bpmn2model_conversationlinks;
    }

    public void addBpmn2model_conversationlink(Bpmn2model_conversationlink bpmn2model_conversationlink) {
        this.bpmn2model_conversationlinks.add(bpmn2model_conversationlink);
    }
    public BPMN2Model_ConversationLink getBpmn2model_conversationlink() {
        return bpmn2model_conversationlink;
    }

    public void setBpmn2model_conversationlink(BPMN2Model_ConversationLink bpmn2model_conversationlink) {
        this.bpmn2model_conversationlink = bpmn2model_conversationlink;
    }
    public BPMN2Model_MessageFlow getBpmn2model_messageflow() {
        return bpmn2model_messageflow;
    }

    public void setBpmn2model_messageflow(BPMN2Model_MessageFlow bpmn2model_messageflow) {
        this.bpmn2model_messageflow = bpmn2model_messageflow;
    }
    public BPMN2Model_ConversationLink getBpmn2model_conversationlink() {
        return bpmn2model_conversationlink;
    }

    public void setBpmn2model_conversationlink(BPMN2Model_ConversationLink bpmn2model_conversationlink) {
        this.bpmn2model_conversationlink = bpmn2model_conversationlink;
    }
    public BPMN2Model_MessageFlow getBpmn2model_messageflow() {
        return bpmn2model_messageflow;
    }

    public void setBpmn2model_messageflow(BPMN2Model_MessageFlow bpmn2model_messageflow) {
        this.bpmn2model_messageflow = bpmn2model_messageflow;
    }
    public List<BPMN2Model_ConversationLink> getBpmn2model_conversationlinks() {
        return bpmn2model_conversationlinks;
    }

    public void addBpmn2model_conversationlink(Bpmn2model_conversationlink bpmn2model_conversationlink) {
        this.bpmn2model_conversationlinks.add(bpmn2model_conversationlink);
    }

}