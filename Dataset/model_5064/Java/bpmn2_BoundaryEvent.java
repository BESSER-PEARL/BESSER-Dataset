





import java.util.List;
import java.util.ArrayList;

public class bpmn2_BoundaryEvent extends CatchEvent {

    private boolean cancelActivity;





    private bpmn2_DocumentRoot bpmn2_documentroot;


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

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}