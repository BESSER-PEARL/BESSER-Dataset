





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Auditing extends BaseElement {






    private BPMN2Model_Process bpmn2model_process;




    private BPMN2Model_FlowElement bpmn2model_flowelement;


    public BPMN2Model_Auditing(
    ) {
        super(
        );
    }



    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }
    public BPMN2Model_FlowElement getBpmn2model_flowelement() {
        return bpmn2model_flowelement;
    }

    public void setBpmn2model_flowelement(BPMN2Model_FlowElement bpmn2model_flowelement) {
        this.bpmn2model_flowelement = bpmn2model_flowelement;
    }

}