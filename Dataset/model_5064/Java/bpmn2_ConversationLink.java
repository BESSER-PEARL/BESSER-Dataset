





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ConversationLink extends BaseElement {






    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_ConversationLink(
    ) {
        super(
        );
    }



    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}