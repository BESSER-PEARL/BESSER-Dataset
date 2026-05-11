





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Artifact extends BaseElement {






    private bpmn2_Collaboration bpmn2_collaboration;




    private bpmn2_SubProcess bpmn2_subprocess;


    public bpmn2_Artifact(
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
    public bpmn2_SubProcess getBpmn2_subprocess() {
        return bpmn2_subprocess;
    }

    public void setBpmn2_subprocess(bpmn2_SubProcess bpmn2_subprocess) {
        this.bpmn2_subprocess = bpmn2_subprocess;
    }

}