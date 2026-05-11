





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Choreography extends FlowElementsContainer, Collaboration {






    private BPMN2Model_Collaboration bpmn2model_collaboration;




    private BPMN2Model_CallChoreography bpmn2model_callchoreography;


    public BPMN2Model_Choreography(
    ) {
        super(
        );
    }



    public BPMN2Model_Collaboration getBpmn2model_collaboration() {
        return bpmn2model_collaboration;
    }

    public void setBpmn2model_collaboration(BPMN2Model_Collaboration bpmn2model_collaboration) {
        this.bpmn2model_collaboration = bpmn2model_collaboration;
    }
    public BPMN2Model_CallChoreography getBpmn2model_callchoreography() {
        return bpmn2model_callchoreography;
    }

    public void setBpmn2model_callchoreography(BPMN2Model_CallChoreography bpmn2model_callchoreography) {
        this.bpmn2model_callchoreography = bpmn2model_callchoreography;
    }

}