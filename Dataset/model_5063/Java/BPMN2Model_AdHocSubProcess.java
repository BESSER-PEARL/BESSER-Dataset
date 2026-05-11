





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_AdHocSubProcess extends SubProcess {

    private String ordering;
    private boolean cancelRemainingInstances;



    public BPMN2Model_AdHocSubProcess(
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


}