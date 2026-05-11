





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_SubProcess extends BPMNActivity, FlowElementsContainer {

    private String triggeredByEvent;



    public BPMNProfile_SubProcess(
        String triggeredByEvent    ) {
        super(
        );
        this.triggeredByEvent = triggeredByEvent;
    }


    public String getTriggeredbyevent() {
        return triggeredByEvent;
    }

    public void setTriggeredbyevent(String triggeredByEvent) {
        this.triggeredByEvent = triggeredByEvent;
    }


}