





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_BoundaryEvent extends CatchEvent {

    private boolean cancelActivity;





    private BPMN2Model_Activity bpmn2model_activity;




    private BPMN2Model_Activity bpmn2model_activity;


    public BPMN2Model_BoundaryEvent(
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

    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }
    public BPMN2Model_Activity getBpmn2model_activity() {
        return bpmn2model_activity;
    }

    public void setBpmn2model_activity(BPMN2Model_Activity bpmn2model_activity) {
        this.bpmn2model_activity = bpmn2model_activity;
    }

}