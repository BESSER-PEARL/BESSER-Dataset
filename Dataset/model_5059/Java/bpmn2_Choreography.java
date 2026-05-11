





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Choreography extends FlowElementsContainer, Collaboration {






    private bpmn2_Collaboration bpmn2_collaboration;


    public bpmn2_Choreography(
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

}