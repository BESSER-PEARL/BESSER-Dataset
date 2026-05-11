





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_AdHocSubProcess extends SubProcess {

    private String ordering;
    private String cancelRemainingInstances;





    private BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression;


    public BPMNProfile_AdHocSubProcess(
        String ordering,        String cancelRemainingInstances    ) {
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
    public String getCancelremaininginstances() {
        return cancelRemainingInstances;
    }

    public void setCancelremaininginstances(String cancelRemainingInstances) {
        this.cancelRemainingInstances = cancelRemainingInstances;
    }

    public BPMNProfile_BPMNExpression getBpmnprofile_bpmnexpression() {
        return bpmnprofile_bpmnexpression;
    }

    public void setBpmnprofile_bpmnexpression(BPMNProfile_BPMNExpression bpmnprofile_bpmnexpression) {
        this.bpmnprofile_bpmnexpression = bpmnprofile_bpmnexpression;
    }

}