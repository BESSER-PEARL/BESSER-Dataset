





import java.util.List;
import java.util.ArrayList;

public class bpmn2_AdHocSubProcess extends SubProcess {

    private String ordering;
    private boolean cancelRemainingInstances;





    private bpmn2_Expression bpmn2_expression;


    public bpmn2_AdHocSubProcess(
        String ordering,        boolean cancelRemainingInstances    ) {
        super(
        );
        this.ordering = ordering;
        this.cancelRemainingInstances = cancelRemainingInstances;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public boolean getCancelremaininginstances() {
        return cancelRemainingInstances;
    }

    public void setCancelremaininginstances(boolean cancelRemainingInstances) {
        this.cancelRemainingInstances = cancelRemainingInstances;
    }

    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}