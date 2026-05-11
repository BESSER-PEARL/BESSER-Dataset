





import java.util.List;
import java.util.ArrayList;

public class bpmn2_MessageFlow extends BaseElement {






    private bpmn2_LaneSet bpmn2_laneset;




    private bpmn2_ConversationNode bpmn2_conversationnode;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_ChoreographyTask bpmn2_choreographytask;




    private bpmn2_Message bpmn2_message;


    public bpmn2_MessageFlow(
    ) {
        super(
        );
    }



    public bpmn2_LaneSet getBpmn2_laneset() {
        return bpmn2_laneset;
    }

    public void setBpmn2_laneset(bpmn2_LaneSet bpmn2_laneset) {
        this.bpmn2_laneset = bpmn2_laneset;
    }
    public bpmn2_ConversationNode getBpmn2_conversationnode() {
        return bpmn2_conversationnode;
    }

    public void setBpmn2_conversationnode(bpmn2_ConversationNode bpmn2_conversationnode) {
        this.bpmn2_conversationnode = bpmn2_conversationnode;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public bpmn2_ChoreographyTask getBpmn2_choreographytask() {
        return bpmn2_choreographytask;
    }

    public void setBpmn2_choreographytask(bpmn2_ChoreographyTask bpmn2_choreographytask) {
        this.bpmn2_choreographytask = bpmn2_choreographytask;
    }
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }

}