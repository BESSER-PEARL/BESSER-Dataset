





import java.util.List;
import java.util.ArrayList;

public class bpmn2_SubProcess extends Activity, FlowElementsContainer {

    private boolean triggeredByEvent;



    public bpmn2_SubProcess(
        boolean triggeredByEvent    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
    }


    public boolean getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(boolean triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }


}