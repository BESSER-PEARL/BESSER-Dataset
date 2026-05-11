





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CompensateEventDefinition extends EventDefinition {

    private boolean waitForCompletion;





    private BPMN2Model_Activity bpmn2model_activity;


    public BPMN2Model_CompensateEventDefinition(
        boolean waitForCompletion    ) {
        super(
        );
        this.waitForCompletion = waitForCompletion;
    }


    public boolean getWaitforcompletion() {
        return waitForCompletion;
    }

    public void setWaitforcompletion(boolean waitForCompletion) {
        this.waitForCompletion = waitForCompletion;
    }

    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }

}