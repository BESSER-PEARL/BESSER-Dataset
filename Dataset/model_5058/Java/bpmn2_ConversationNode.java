





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ConversationNode extends BaseElement, InteractionNode {

    private String name;





    private bpmn2_Collaboration bpmn2_collaboration;


    public bpmn2_ConversationNode(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_Collaboration getBpmn2_collaboration() {
        return bpmn2_collaboration;
    }

    public void setBpmn2_collaboration(bpmn2_Collaboration bpmn2_collaboration) {
        this.bpmn2_collaboration = bpmn2_collaboration;
    }

}