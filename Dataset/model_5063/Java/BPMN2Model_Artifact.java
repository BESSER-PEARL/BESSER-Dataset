





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Artifact extends BaseElement {






    private BPMN2Model_SubChoreography bpmn2model_subchoreography;




    private BPMN2Model_Process bpmn2model_process;




    private BPMN2Model_SubProcess bpmn2model_subprocess;


    public BPMN2Model_Artifact(
    ) {
        super(
        );
    }



    public BPMN2Model_SubChoreography getBpmn2model_subchoreography() {
        return bpmn2model_subchoreography;
    }

    public void setBpmn2model_subchoreography(BPMN2Model_SubChoreography bpmn2model_subchoreography) {
        this.bpmn2model_subchoreography = bpmn2model_subchoreography;
    }
    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }
    public BPMN2Model_SubProcess getBpmn2model_subprocess() {
        return bpmn2model_subprocess;
    }

    public void setBpmn2model_subprocess(BPMN2Model_SubProcess bpmn2model_subprocess) {
        this.bpmn2model_subprocess = bpmn2model_subprocess;
    }

}