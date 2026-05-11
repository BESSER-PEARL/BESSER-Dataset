





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Choreography extends FlowElementsContainer, Collaboration {






    private bpmn2_CallChoreography bpmn2_callchoreography;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Choreography(
    ) {
        super(
        );
    }



    public bpmn2_CallChoreography getBpmn2_callchoreography() {
        return bpmn2_callchoreography;
    }

    public void setBpmn2_callchoreography(bpmn2_CallChoreography bpmn2_callchoreography) {
        this.bpmn2_callchoreography = bpmn2_callchoreography;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}