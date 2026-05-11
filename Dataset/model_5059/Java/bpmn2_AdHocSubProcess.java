





import java.util.List;
import java.util.ArrayList;

public class bpmn2_AdHocSubProcess extends SubProcess {

    private boolean cancelRemainingInstances;
    private String ordering;





    private bpmn2_Expression bpmn2_expression;


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

    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}