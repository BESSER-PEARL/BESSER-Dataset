





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_AdHocSubProcess extends SubProcess {

    private String cancelRemainingInstances;
    private String ordering;





    private bpmnprof_BPMNExpression bpmnprof_bpmnexpression;


    public bpmnprof_AdHocSubProcess(
        String cancelRemainingInstances,        String ordering    ) {
        super(
        );
        this.cancelRemainingInstances = cancelRemainingInstances;
        this.ordering = ordering;
    }


    public String getCancelremaininginstances() {
        return cancelRemainingInstances;
    }

    public void setCancelremaininginstances(String cancelRemainingInstances) {
        this.cancelRemainingInstances = cancelRemainingInstances;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }

    public bpmnprof_BPMNExpression getBpmnprof_bpmnexpression() {
        return bpmnprof_bpmnexpression;
    }

    public void setBpmnprof_bpmnexpression(bpmnprof_BPMNExpression bpmnprof_bpmnexpression) {
        this.bpmnprof_bpmnexpression = bpmnprof_bpmnexpression;
    }

}