





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CompensateEventDefinition extends EventDefinition {

    private boolean waitForCompletion;





    private bpmn2_Activity bpmn2_activity;


    public bpmn2_CompensateEventDefinition(
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

    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }

}