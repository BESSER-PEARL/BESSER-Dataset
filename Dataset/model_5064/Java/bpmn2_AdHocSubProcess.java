





import java.util.List;
import java.util.ArrayList;

public class bpmn2_AdHocSubProcess extends SubProcess {

    private boolean cancelRemainingInstances;
    private String ordering;





    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_AdHocSubProcess(
        boolean cancelRemainingInstances,        String ordering    ) {
        super(
        );
        this.cancelRemainingInstances = cancelRemainingInstances;
        this.ordering = ordering;
    }


    public boolean getCancelremaininginstances() {
        return cancelRemainingInstances;
    }

    public void setCancelremaininginstances(boolean cancelRemainingInstances) {
        this.cancelRemainingInstances = cancelRemainingInstances;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }

}