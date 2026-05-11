





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_SubProcess extends FlowElementsContainer, Activity {

    private boolean triggeredByEvent;



    public BPMN2Model_SubProcess(
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