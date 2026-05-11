





import java.util.List;
import java.util.ArrayList;

public class bpmn2_BoundaryEvent extends CatchEvent {

    private boolean cancelActivity;





    private bpmn2_Activity bpmn2_activity;




    private bpmn2_Activity bpmn2_activity;


    public bpmn2_BoundaryEvent(
        boolean cancelActivity    ) {
        super(
        );
        this.cancelActivity = cancelActivity;
    }


    public boolean getCancelactivity() {
        return cancelActivity;
    }

    public void setCancelactivity(boolean cancelActivity) {
        this.cancelActivity = cancelActivity;
    }

    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }
    public bpmn2_Activity getBpmn2_activity() {
        return bpmn2_activity;
    }

    public void setBpmn2_activity(bpmn2_Activity bpmn2_activity) {
        this.bpmn2_activity = bpmn2_activity;
    }

}