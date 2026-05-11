





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CompensateEventDefinition extends EventDefinition {

    private boolean waitForCompletion;



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


}